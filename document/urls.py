from django.urls import path
from django.conf.urls import url
from document import views

urlpatterns = [
    url(r'^approve_document/(?P<document_id>\d+)/(?P<next_state_id>\d+)/$', views.approve_document, name='approve_document'),
    path('', views.documents, name='home'),
    path('documents', views.documents, name='documents'),
    url(r'documents_list', views.documents_list, name='documents_list'),
    path('documents/<str:doc_id>', views.document_detail, name='document_detail'),

    path('upload_document', views.upload_document, name="upload_document"),
    path('download/<str:doc_id>', views.download_file, name='download'),

    path('load_reviewer', views.load_reviewer, name='load_reviewer'),
    path('my_documents', views.my_documents, name='my_documents'),
    path('my_documents/<str:doc_id>', views.my_doc_detail, name='my_doc_detail'),
    path('my_documents/<str:doc_id>/change', views.my_doc_change, name='my_doc_change'),

    path('inbox', views.inbox, name='inbox'),
    path('inbox/<str:doc_id>', views.inbox_detail, name='inbox_detail'),
]
