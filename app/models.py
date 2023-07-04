from django.db import models

# Create your models here.

class Proinfo(models.Model):

    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)

class Product(models.Model):

    asingtin=models.CharField(max_length=14)
    title=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    rating=models.CharField(max_length=20)
    stock=models.CharField(max_length=10)

