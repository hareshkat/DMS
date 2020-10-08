from django.db import models

# Create your models here.
from river.models.fields.state import StateField
from employee.models import DmsUser, Department
import uuid
import os
from django.utils.safestring import mark_safe



class Document(models.Model):
    no = models.CharField("Ticket Number", max_length=50, default=uuid.uuid4, null=False, blank=False, editable=False,
                          unique=True)

    title = models.CharField("Title", max_length=500)
    owner = models.ForeignKey(DmsUser, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='docss')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    reviewed_by = models.ForeignKey(DmsUser, on_delete=models.DO_NOTHING, related_name='reviewed_by', verbose_name='Reviewed by')
    approved_by = models.ForeignKey(DmsUser, on_delete=models.DO_NOTHING, related_name='approve_by', verbose_name='Approved by', null=True, blank=True)
    date =  models.DateTimeField(auto_now_add=True)
    status = StateField(editable=True)

    def natural_key(self):
        return self.no

    def filename(self):
        return os.path.basename(self.file.name)

    def file_download(self):
        url = "<a href='/download/"+str(self.no)+"'>"
        return mark_safe(url+"<i class='nav-icon fa fa-download text-success'></i></a>")

    def file_name(self):
        return os.path.basename(self.file.url)


class Document_comment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING)
    comment = models.TextField(max_length=500, null=True, blank=True)
    comment_owner = models.ForeignKey(DmsUser, on_delete=models.DO_NOTHING)
    date =  models.DateTimeField(auto_now_add=True)
