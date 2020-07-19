from colorfield.fields import ColorField
from django.db import models


class Diary(models.Model):
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    color = ColorField(default='#FF0000')
