from django.conf.urls import url
from auth import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]