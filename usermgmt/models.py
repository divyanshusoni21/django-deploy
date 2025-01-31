from django.db import models

# Create your models here.

class test(models.Model):
    field = models.CharField(max_length=20)
    