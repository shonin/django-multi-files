from django.contrib.auth.forms import AuthenticationForm
from django import forms
from multiupload.fields import MultiFileField

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))



class UploadForm(forms.Form):
    # If you need to upload media files, you can use this:
    attachments = MultiFileField(
        min_num=1,
        max_num=3,
        max_file_size=1024*1024*10,
    )

class EditFileForm(forms.Form):
    name = forms.CharField(label="File Name", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'file name'}))
    description = forms.Textarea()