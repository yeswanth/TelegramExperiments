from django.db import models

# Create your models here.
class HomeWorkModel(models.Model):
    desc = models.CharField(max_length=300)
    tag = models.CharField(max_length=100,null=True,blank=True)
