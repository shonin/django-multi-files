from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

import boto3

from drinking_gourd.models import File
from drinking_gourd.forms import UploadForm, EditFileForm
from drinking_gourd.helpers.s3_helper import upload_file


@login_required(login_url="login/")
def home(request):
    files = File.objects.all()
    return render(request,"home.html", {'files':files})

class EditFileView(LoginRequiredMixin, UpdateView):
    model = File
    fields = ['name', 'description']
    template_name = 'edit_file.html'
    success_url = '/drinkinggourd/'

class UploadView(LoginRequiredMixin, FormView):
    template_name = 'uploads/form.html'
    form_class = UploadForm
    success_url = '/drinkinggourd/'

    def form_valid(self, form):
        for file in form.cleaned_data['attachments']:

            file_object = File.objects.create(name=file.name)
            upload_file(file, file_object.key)

        return super(UploadView, self).form_valid(form)