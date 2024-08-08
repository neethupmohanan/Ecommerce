from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=50)

class product(models.Model):
   proname = models.CharField(max_length=50)
   price = models.IntegerField()
   image = models.ImageField(upload_to='images')
   quantity = models.IntegerField()


class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   products = models.ForeignKey(product, on_delete=models.CASCADE)
   image=models.ImageField(upload_to='images')
   price = models.IntegerField()
   quantity = models.IntegerField()


   class name(models.Model):
      name=models.CharField(max_length=50)

class address(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   housename=models.CharField(max_length=50)
   roadname=models.CharField(max_length=50)
   pincode=models.IntegerField()
   city=models.CharField(max_length=50)
   state=models.CharField(max_length=50)
   contact=models.CharField(max_length=10)


class order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   products = models.ForeignKey(product, on_delete=models.CASCADE)
   address = models.ForeignKey(address, on_delete=models.CASCADE)
   price=models.IntegerField()
   quantity=models.IntegerField()





