from django.db import models
from django.contrib.postgres.fields import ArrayField

class Game(models.Model):
    appid = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=500)
    img_icon_url = models.CharField(max_length=100)
    tags = ArrayField(
        base_field=models.CharField(max_length=100, blank=True, default=list)
    )