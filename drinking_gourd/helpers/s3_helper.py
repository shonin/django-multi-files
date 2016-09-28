import boto3
from django.conf import settings

BUCKET = settings.BUCKET

def upload_file(file, folder):
    s3 = boto3.resource('s3')
    path = '{file}'.format(folder=folder, file=file)
    s3.Object(BUCKET, file).put(Body=open(path, 'rb'))


def read_all_files():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)

    dict = {}

    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()

        dict[key] = body

    return dict

def list_files():
    files = []
    objs = boto3.client(Bucket=BUCKET)
    while 'Contents' in objs.keys():
        objs_contents = objs['Contents']
        for i in range(len(objs_contents)):
            filename = objs_contents[i]['Key']
            files += filename

    return files