# Django & Javascript Multi File Upload to S3

*A Django app that uploads multiple files at once to Amazon S3 using javascript.
Built to run on Heroku, and started from [Heroku's Django Starter
 Template](https://github.com/heroku/heroku-django-template), nice template,
thanks.*

*The majority of the underlying logic comes from @flyingsparx's
[FlaskDirectUploader](https://github.com/flyingsparx/FlaskDirectUploader),
and his guide for it
 [here](https://devcenter.heroku.com/articles/s3-upload-python).*

## What this is:

This is a basic Django application that is doing essentially two things.
1. The Django app is told about the selected files and returns a set of
validation data to the client
2. The client sends the validated request directly to your Amazon S3 Bucket

This comes with a lot of prebundled things that make this mostly ready to


## But what is it really?

* `python 3.4`
* `django 1.9`
* `boto3`

***

# Get It Up and Running:

***

## AWS Trickery:

### Setup a Bucket in S3 with Correct Permissions:

In AWS go to S3, and then create a new bucket. give it a name.   

** Bucket -> Properites -> Permissions -> Edit CORS Configuration**  

*Here is an example CORS configuration, you should probably have some more
security on yours, but this is fine for development*
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>

```
If this isn't setup right you'll get errors on the upload saying `NotAllowed`
or something similar

### Get your Access Key and Secret Access Key

I'm far from an AWS expert, but this is in IAM, go in there an make a new
user, ***get the users keys***, and attach the policy `AmazonS3FullAccess` to the user.

***

## Setup the Django App

uhhh... you have `virtualenv`, right?

```shell
$ mkvirtualenv multi-file
(multi-file) $ git clone https://github.com/shonin/django-multi-files.git
(multi-file) $ cd django-multi-files/
(multi-file) $ pip install -r requirements.txt
(multi-file) $ python manage.py makemigrations
(multi-file) $ python manage.py migrate
```
### Gonna need some env vars

*How you wanna do this is up to you, I use PyCharm.*

***An excerpt from `settings.py`***
```python
import os
...
BUCKET = os.getenv('AWS_BUCKET_NAME')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
...
```
Those are the things you need for `boto3` to be able to do it's magic.

***

# Final Notes

That's pretty much it. Checkout the `direct.html` file to see the javascript
and look at the `sign_s3` view see how the python handles the request.

*My javascript is pretty rough and hacked together. You might want to do
something better with this for production*

To see how I'm using this with some django auth for handling raw podcast data,
see my [DrinkingGourd repo here](https://github.com/shonin/DrinkingGourd)

If you have any issues getting this running, feel free to open an issue, I'm
happy to help.

Improvements? Open a PR!
