from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=128,unique=True)