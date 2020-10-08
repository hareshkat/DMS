import django_tables2 as tables
from .models import Document
from django_tables2 import A


class DocumentTable(tables.Table):
    title = tables.LinkColumn("document_detail", args=[A("no")])
    download = tables.Column(accessor='file_download', verbose_name='Download')
    file_name = tables.Column(accessor='file_name', verbose_name='File')
    class Meta:
        model = Document
        fields = ['title', 'owner', 'file_name', 'date', 'download']


class MyDocumentTable(tables.Table):
    title = tables.LinkColumn("my_doc_detail", args=[A("no")])
    download = tables.Column(accessor='file_download', verbose_name='Download')
    file_name = tables.Column(accessor='file_name', verbose_name='File')
    class Meta:
        model = Document
        fields = ['title', 'file_name', 'status', 'date', 'download']


class InboxTable(tables.Table):
    title = tables.LinkColumn("inbox_detail", args=[A("no")])
    download = tables.Column(accessor='file_download', verbose_name='Download')
    file_name = tables.Column(accessor='file_name', verbose_name='File')
    class Meta:
        model = Document
        fields = ['title', 'owner', 'file_name', 'status', 'date', 'download']
