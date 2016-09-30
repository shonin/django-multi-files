import json
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import boto3

from uploader.models import File
from uploader.helpers.s3_helper import delete_file

S3_BUCKET = settings.BUCKET

def direct(request):
    if not request.POST:
        return render(request, "uploads/direct.html", {'S3_BUCKET': S3_BUCKET})
    else:
        File.objects.create(name=request.POST.get('name'))
        return HttpResponseRedirect('/')

@csrf_exempt
def sign_s3(request):
    if request.method == 'GET':
        file_name = request.GET.get('file-name')
        file_type = request.GET.get('file-type')

        file = File.objects.create(name=file_name)
        key = file.key

        file_url = 'https://s3.amazonaws.com/{bucket}/{key}'.format(bucket=S3_BUCKET, key=key)
        url = 'https://s3.amazonaws.com/{bucket}'.format(bucket=S3_BUCKET)

        s3 = boto3.client('s3')

        presigned_post = s3.generate_presigned_post(
            Bucket=S3_BUCKET,
            Key=key,
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=3600,
        )

        presigned_post['url'] = url

        return HttpResponse(json.dumps({
            'data': presigned_post,
            'url': file_url
        }))
    else:
        return HttpResponse('got a POST request')


def home(request):
    files = File.objects.all()
    for file in files:
        try:
            file.upload_date = file.upload_date.strftime('%b. %d, %Y')
        except Exception as e:
            print('\n\nEXCEPTION - Could not get date: {e}'.format(e=e))
            file.upload_date = 'whoops'

    return render(request, "home.html", {'files': files})


class EditFileView(UpdateView):
    model = File
    fields = ['name', 'description']
    template_name = 'edit_file.html'
    success_url = '/'

class DeleteFileView(DeleteView):
    model = File
    template_name = 'delete_file.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        delete_file(self.object.key)
        return HttpResponseRedirect(success_url)
