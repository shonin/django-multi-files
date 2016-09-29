# Drinking Gourd

*A Django app built to run on Heroku, started from [Heroku's Django Starter
 Template](https://github.com/heroku/heroku-django-template), nice template,
thanks.*

## What this is:

Users log in and upload files that get put in S3. Users can then edit the
file to change the name and add a description. They can delete the file, which
will also remove it from S3.

Meant to be used to manage pre-production podcast recordings

## But what is it really?

* Django Auth
* Boto3 to wrap the S3 API
* Direct to S3 uploads via javascript, preferable to having an open connection
to the server while yuge files upload.
* Bootstrap and jQuery
* [WhiteNoise](https://warehouse.python.org/project/whitenoise/) for handling
static assets on Heroku

## What does the future hold?

* Upload multiple files at once
* Upload file type protection to allow only `.wma` and `.mp3`
* Convert WMA's to MP3's
* Automatically add an into and an exit to an MP3 file
* Upload finished podcast files to a [Libsyn](http://www.libsyn.com) FTP Server
and schedule them for publication.
* integrate a proper user facing site that plays the podcasts, like the one
that I already built [here](drinkinggourd.herokuapp.com).

#### thanks

* [Heroku's Django Starter
 Template](https://github.com/heroku/heroku-django-template)
* @flyingsparx's  [FlaskDirectUploader](https://github.com/flyingsparx/FlaskDirectUploader)
for a solid example of direct to s3 uploads using python and boto3
* @narenaryan's blog post on using [Django's built in Auth](https://github.com/narenaryan/django-auth-pattern)
