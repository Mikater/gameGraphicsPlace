from django.db import models
from datetime import datetime


class GraphicPack(models.Model):
    packName = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    theme = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    title_img = models.ImageField()
    files_id = models.IntegerField()
    datetime = models.DateTimeField(default=datetime.now())
