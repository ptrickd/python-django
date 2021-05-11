from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120, default='')
    content = models.TextField(default='')
    active = models.BooleanField(default=True)