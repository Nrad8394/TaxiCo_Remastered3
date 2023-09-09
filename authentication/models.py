from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    pickup_time = models.DateTimeField()
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    taxi = models.ForeignKey('Taxi', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    passengers = models.IntegerField(null=True,blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pickup_location + " - "+ self.dropoff_location
    
    class Meta:
        ordering = ['create_time']

class register(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
     First_name = models.CharField(max_length=200)
     last_name = models.CharField(max_length=200)
     job_choice = models.TextChoices('Driver','Carowner')
     phone_number = models.IntegerField()
     email = models.EmailField(max_length=254)
     address = models.CharField(max_length=255)
     slight_description = models.TextField(max_length=500)
     
class Taxi(models.Model):
    driver_name = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    active = models.BooleanField()
    
    