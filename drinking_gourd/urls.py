from django.conf.urls import url
from drinking_gourd import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]