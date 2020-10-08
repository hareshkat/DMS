from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from employee.models import DmsUser, Department
from .tables import DmsUserTable, DepartmentTable, DeptEmpsTable
from django.http import HttpResponse
from django_tables2 import RequestConfig


# Create your views here.
def login_view(request):
  if request.user.id != None:
    return redirect("/")
  else:
    msg = ''
    if request.method == 'POST':
      username = request.POST['username']
      password =  request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
          msg = 'Invalid credentials'
    return render(request, "account/login.html", {'msg':msg})


@login_required(login_url="/login/")
def employees_list(request):
    user_table = DmsUserTable(DmsUser.objects.all())
    RequestConfig(request).configure(user_table)
    user_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return HttpResponse(user_table.as_html(request))


@login_required(login_url="/login/")
def employees(request):
    return render(request, "employee/employees.html")


@login_required(login_url="/login/")
def departments_list(request):
    department_table = DepartmentTable(Department.objects.all())
    RequestConfig(request).configure(department_table)
    department_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return HttpResponse(department_table.as_html(request))


@login_required(login_url="/login/")
def departments(request):
    return render(request, "employee/departments.html")


@login_required(login_url="/login/")
def department_employees(request, dept_id):
    data = DmsUser.objects.values().filter(department=dept_id)
    dept_emps_table = DeptEmpsTable(DmsUser.objects.all().filter(department=dept_id))
    RequestConfig(request).configure(dept_emps_table)
    dept_emps_table.paginate(page=request.GET.get("page", 1), per_page=5)
    return render(request, "employee/departments_employees.html", {'data':dept_emps_table, 'department':dept_id})
