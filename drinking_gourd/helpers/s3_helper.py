import boto3
from django.conf import settings

BUCKET = settings.BUCKET

def upload_file(file, key):
    try:
        file_name = key
        file_content = file.read()
        s3 = boto3.resource('s3')
        s3.Object(BUCKET, file_name).put(Body=file_content)
        return True
    except Exception as e:
        print("ERROR: There was an error uploading the file: {e}".format(e=e))

def read_file(key):
    s3 = boto3.resource('s3')
    file_contents = s3.Object(BUCKET, key).get()['Body'].read()
    return file_contents

def delete_file(key):
    s3 = boto3.resource('s3')
    s3.Object(BUCKET, key).delete()


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