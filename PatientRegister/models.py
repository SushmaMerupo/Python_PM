from django.db import models

# Create your models here.
class patient(models.Model):
    Username=models.CharField(max_length=100)
    Userid=models.IntegerField()
    DoJ=models.DateField()
