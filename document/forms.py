from django.forms import ModelForm
from .models import Document
from django import forms
from employee.models import Department

class DocumentUploadForm(ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'file', 'department', 'reviewed_by']
