from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from drinking_gourd.models import File
from drinking_gourd.forms import UploadForm
from drinking_gourd.helpers.s3_helper import upload_file, delete_file


@login_required(login_url="login/")
def home(request):
    files = File.objects.all()
    return render(request,"home.html", {'files':files})

class EditFileView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = File
    fields = ['name', 'description']
    template_name = 'edit_file.html'
    success_url = '/drinkinggourd/'

class UploadView(LoginRequiredMixin, FormView):
    login_url = '/login/'

    template_name = 'uploads/form.html'
    form_class = UploadForm
    success_url = '/drinkinggourd/'

    def form_valid(self, form):
        for file in form.cleaned_data['attachments']:

            file_object = File.objects.create(name=file.name)
            upload_file(file, file_object.key)

        return super(UploadView, self).form_valid(form)

class DeleteFileView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = File
    template_name = 'delete_file.html'
    success_url = '/drinkinggourd/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        delete_file(self.object.key)
        return HttpResponseRedirect(success_url)