from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import boto3

@login_required(login_url="login/")
def home(request):
    s3 = boto3.resource('s3')
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket)
    return render(request,"home.html", {'buckets':buckets})
