from django.db import models


# Create your models here.

class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    productname=models.CharField(max_length=50)
    mfgdate=models.CharField(max_length=30)
    expdate=models.CharField(max_length=30)
    price=models.IntegerField()
    productpic=models.FileField(upload_to='')