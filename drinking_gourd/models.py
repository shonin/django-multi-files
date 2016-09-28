from time import gmtime, strftime
from django.db import models

class File(models.Model):
    # file = models.FileField(upload_to=upload_file(), blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    upload_date = models.CharField(max_length=100, default=strftime("%Y%m%d%H%M%S", gmtime()))
    key = models.CharField(max_length=600, blank=True)

    def __str__(self):
        representation = '{name}__{date}'.format(name=self.name, date=self.upload_date)
        return representation

    def generate_key(self):
        key = '{date}__{name}'.format(date=self.upload_date, name=self.name)
        return key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super(File, self).save(*args, **kwargs)