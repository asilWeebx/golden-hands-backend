from django.db import models

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')

class Contact(models.Model):
    phone_1 = models.CharField(max_length=100)
    phone_2 = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    