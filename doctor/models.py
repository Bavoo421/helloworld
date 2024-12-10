from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    specialization = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True, blank=True)

# Create your models here.
