from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http.response import HttpResponse, Http404
from river.models import State
from .models import Document, Document_comment
from .tables import DocumentTable, MyDocumentTable, InboxTable
from django_tables2 import RequestConfig
from .forms import DocumentUploadForm
from employee.models import Department, DmsUser
from django.utils.safestring import mark_safe
import os
from django.conf import settings
from django import forms
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
from river.models import State

from document.models import Document


@login_required(login_url="/login/")
def approve_document(request, document_id, next_state_id=None):
    document = get_object_or_404(Document, pk=document_id)
    next_state = get_object_or_404(State, pk=next_state_id)

    try:
        document.river.status.approve(as_user=request.user, next_state=next_state)
        if (request.method == 'GET') and (next_state_id == '5'):
            comment = request.GET['review_comment']
            doc_id = request.GET['doc_id']
            doc_comment = Document_comment(document_id = doc_id, comment = comment, comment_owner_id = request.user.id)
            doc_comment.save()
        if (request.method == 'GET') and (next_state_id == '4'):
            approver_id = request.GET['approver']
            doc_id = request.GET['doc_id']
            doc_instance = Document.objects.filter(pk = doc_id).get()
            doc_instance.approved_by_id = approver_id
            doc_instance.save()
        return redirect('inbox')
    except Exception as e:
        return HttpResponse(e)


@login_required(login_url="/login/")
def documents_list(request):
    doc_table = DocumentTable(Document.objects.all().filter(status=6))
    RequestConfig(request).configure(doc_table)
    doc_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return HttpResponse(doc_table.as_html(request))


@login_required(login_url="/login/")
def documents(request):
    search = request.GET.get('search', None)
    my_doc_table = {}
    if search is not None:
        my_doc_table = DocumentTable(Document.objects.all().filter(status=6).filter(
            Q(title__icontains=search) | Q(file__icontains=search)
        ))
        my_doc_table.paginate(page=request.GET.get("page", 1), per_page=5)
        return render(request, "document/documents_search.html", {'search_data':my_doc_table})
    else:
        return render(request, "document/documents.html")


@login_required(login_url="/login/")
def document_detail(request, doc_id):
    doc_data = Document.objects.filter(no=doc_id).values().first()
    return render(request, "document/document_detail.html", {'data':doc_data})


@login_required(login_url="/login/")
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        docx = form.save(commit=False)
        docx.owner_id = request.user.id
        if form.is_valid():
            form.save()
            return redirect('my_documents')
        else:
            return render(request, "document/upload_doc.html", {'form':form})
    else:
        form = DocumentUploadForm()
        choices_default = ('', '---------'),
        choices = tuple(Department.objects.filter(dmsuser = request.user.id).values_list('dept_no','dept_name'))
        final_choice = choices_default + choices
        form.fields["department"] = forms.ChoiceField(choices = final_choice)
        return render(request, "document/upload_doc.html", {'form':form})


@login_required(login_url="/login/")
def load_reviewer(request):
    dept_id = request.GET.get('department')
    reviewers = DmsUser.objects.filter(department=dept_id, groups=2).values()
    return render(request, 'document/reviewers_list_options.html', {'reviewers': reviewers})


@login_required(login_url="/login/")
def my_documents(request):
    my_doc_table = MyDocumentTable(Document.objects.filter(owner_id=request.user.id).order_by('-date').all())
    # RequestConfig(request).configure(my_doc_table)
    my_doc_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return render(request, "document/my_documents.html", {'data':my_doc_table})


@login_required(login_url="/login/")
def inbox(request):
    inbox_table = InboxTable(Document.objects.filter(Q(reviewed_by_id = request.user.id) | Q(approved_by_id = request.user.id)).exclude(status_id=1).order_by('-date').all())
    # RequestConfig(request).configure(inbox_table)
    inbox_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return render(request, "document/inbox.html", {'data':inbox_table})


@login_required(login_url="/login/")
def inbox_detail(request, doc_id):
    doc_detail = Document.objects.filter(no=doc_id).values().first()
    obj = Document.objects.get(no=doc_id)
    actions = river_actions(obj, request)
    return render(request, "document/inbox_detail.html", {'data':doc_detail, 'xyz':actions})


@login_required(login_url="/login/")
def my_doc_detail(request, doc_id):
    doc_detail = Document.objects.filter(no=doc_id).values().first()
    doc_comment = Document_comment.objects.values().filter(document_id = doc_detail['id']).order_by('-date')
    return render(request, "document/my_doc_detail.html", {'data':doc_detail, 'comments':doc_comment})


@login_required(login_url="/login/")
def download_file(request, doc_id):
    data = Document.objects.filter(no=doc_id).values().first()
    file_path = os.path.join(settings.MEDIA_ROOT, data['file'])
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url="/login/")
def my_doc_change(request, doc_id):
    if request.method == 'POST':
        instance = Document.objects.get(no=doc_id)
        form = DocumentUploadForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_doc_detail', doc_id=doc_id)
        else:
            return render(request, "employee/department_change.html", {'form':form, 'data':instance})
    else:
        data = Document.objects.get(no=doc_id)
        form = DocumentUploadForm(instance=data)
        return render(request, "document/my_doc_change.html", {'form':form, 'data':data})


def create_river_button(obj, transition_approval):
    approve_ticket_url = reverse('approve_document', kwargs={'document_id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    if transition_approval.transition.destination_state.pk == 5 :
        return f"""
            <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#myModal4">
            {transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}
            </button>

            <div class="modal fade" id="myModal4" role="dialog">
              <div class="modal-dialog modal-lg">
                <div class="modal-content">
                  <div class="modal-body">
                    <form action="{approve_ticket_url}" method="get">
                      <div class="form-group">
                        <span class="col-form-label">Add your comments before putting this document into clarify</span>
                        <textarea type="text" class="form-control" name="review_comment" required></textarea>
                      </div>
                      <input type="text" value="{ obj.pk }" hidden class="form-control" name="doc_id">
                      <button class="btn btn-danger">Clarify</button>
                      <button class="btn btn-warning" data-dismiss="modal">Close</button>
                    </form>
                  </div>
                </div>
              </div>
            </div>
        """
    elif transition_approval.transition.destination_state.pk == 4:
        approvers = DmsUser.objects.filter(groups=3, department = obj.department).values()
        options = "<option value="" >---------</option>"
        for approver in approvers:
            options += "<option value='" + str(approver['id']) +"'>"+ approver['username'] +"</option>"

        return f"""
            <button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal3">
            {transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}
            </button>

            <div class="modal fade" id="myModal3" role="dialog">
              <div class="modal-dialog modal-lg">
                <div class="modal-content">
                  <div class="modal-body">
                      <h5 class="modal-title">Are you sure you want to review this document ?</h5><br>
                      <form action="{approve_ticket_url}" method="get">
                          <div class="form-group">
                              <label for="id_department">Select aprover</label>
                              <select name="approver" class="form-control" title="" required="" id="id_approved_by">
                              {options}
                              </select>
                          </div>
                          <input type="text" value="{ obj.pk }" hidden class="form-control" name="doc_id">
                          <button class="btn btn-info">Review</button>
                          <button class="btn btn-warning" data-dismiss="modal">Close</button>
                      </form>
                  </div>
                </div>
              </div>
            </div>
        """
    elif transition_approval.transition.destination_state.pk == 6:
        return f"""
            <button type="button" class="btn btn-success" data-toggle="modal" data-target="#myModal5">
            {transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}
            </button>

            <div class="modal fade" id="myModal5" role="dialog">
              <div class="modal-dialog modal-lg">
                <div class="modal-content">
                  <div class="modal-body">
                      <h5 class="modal-title">Are you sure you want to approve this document ?</h5><br>
                        <input type="button" class="btn btn-success" value="Approve"
                            onclick="location.href=\'{approve_ticket_url}\'"/>
                      <button class="btn btn-warning" data-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
        """
    else:
        return f"""
        <input
            type="button"
            class="btn btn-warning"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_ticket_url}\'"
        />
    """


def river_actions(obj, request):
    content = ""
    for transition_approval in obj.river.status.get_available_approvals(as_user=request.user):
        content += create_river_button(obj, transition_approval)
    return mark_safe(content)
