from django.conf.urls import url
from drinking_gourd import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^edit/(?P<pk>[0-9]+)/', views.EditFileView.as_view(), name='edit_file'),
    url(r'^delete/(?P<pk>[0-9]+)/', views.DeleteFileView.as_view(), name='delete_file'),
    url(r'^upload', views.UploadView.as_view(), name='upload'),
]