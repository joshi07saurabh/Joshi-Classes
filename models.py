from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField(max_length=10)
    subject = models.CharField(max_length=20)
    address = models.CharField(max_length=120)

