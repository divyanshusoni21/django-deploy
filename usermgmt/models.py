from django.db import models

# Create your models here.

class test(models.Model):
    field = models.CharField(max_length=20)
    new_field = models.CharField(max_length=200,blank=True)