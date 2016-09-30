from django.db import models
from django.utils import timezone

class File(models.Model):
    name = models.CharField(max_length=300)
    upload_date = models.DateTimeField(editable=False)
    key = models.CharField(max_length=600, blank=True)

    def __str__(self):
        representation = '{name}__{date}'.format(name=self.name, date=self.upload_date)
        return representation

    def generate_key(self):
        time = self.upload_date.strftime('%Y%m%d_%H%M%S_%f')
        key = '{time}__{name}'.format(time=time, name=self.name)
        return key

    def save(self, *args, **kwargs):
        if not self.id:
            self.upload_date = timezone.now()
        if not self.key:
            self.key = self.generate_key()
        super(File, self).save(*args, **kwargs)