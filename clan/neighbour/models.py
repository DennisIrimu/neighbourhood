from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

# Create your models here.

class UserProfile(models.Model):
    '''
    User class to save app user data
    '''

    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True )
    name = models.CharField(max_length = 100,null = True)
    identification = models.IntegerField(null = True)
    neighbourhood = models.ForeignKey
    location = models.CharField(max_length = 100,null = True)
    avatar = models.ImageField(upload_to = 'avatar/',null = True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

class Neighborhood(models.Model):
    '''
    class for saving neighbourhood data
    '''
    name  = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupant_count = models.IntegerField()
    def __str__(self):
        return self.name
    def save_neighborhood(self):
        self.save()

class Business(models.Model):
    '''
    model that displays businesses in a certain area
    '''
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null=True)
    email= models.CharField(max_length = 100)
    def __str__(self):
       return self.name

    def save_business(self):
        self.save()

class Post(models.Model):
   '''
   model that saves posts for the neighborhood
   '''
   title = models.CharField(max_length  = 100,null = True)
   post = models.TextField(max_length=100,null = True)
   profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   time = models.DateTimeField(auto_now_add=True,null = True)

class Services(models.Model):
   '''
   model that saves the services data
   '''
   police_station = models.CharField(max_length = 30,blank = True)
   police_no = models.IntegerField(10,blank = True)
   police_location = models.CharField(max_length = 30,blank = True)
   healthcare_centre = models.CharField(max_length = 30,blank = True)
   healthcare_no = models.IntegerField(10,blank = True)
   healthcare_location = models.CharField(max_length = 30 ,blank = True)
