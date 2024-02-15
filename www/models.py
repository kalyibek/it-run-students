import os
from django.db import models
from django.conf import settings

import os

IMAGES_ROOT = os.path.relpath(os.path.join(settings.MEDIA_ROOT, 'images'))


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    characteristics = models.TextField(null=True)
    photo = models.ImageField(upload_to=IMAGES_ROOT, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
