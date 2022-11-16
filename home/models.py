from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class Car(models.Model):
    number_plate = models.CharField(max_length=200)
    model= models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.number_plate
class User(AbstractUser):
   
    cars = models.ForeignKey(Car, related_name="owner", on_delete=models.CASCADE)
    
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    ph_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)


    

    




class Ads(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    vehcile = models.ForeignKey(Car, on_delete=models.PROTECT)


    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_km = models.IntegerField()
  



