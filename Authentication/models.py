from asyncio.windows_events import NULL
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model 

# Create your models here.

class user_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    # firstname = models.CharField(max_length=50)
    midelname = models.CharField(max_length=50)
    # lastname = models.CharField(max_length=50)
    suffix = models.CharField(max_length=50)
    # email =  models.EmailField(max_length=30)
    last_snn = models.CharField(max_length=4)
    dob = models.DateField(default=NULL)
    

    phone_h =  models.CharField(max_length=15)
    phone_w =  models.CharField(max_length=15)
    phone_m =  models.CharField(max_length=15)
    fax = models.CharField(max_length=25)
    mail_address = models.TextField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode= models.CharField(max_length=15)



    def __str__(self):
        return str(self.user)

class providerdetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    p_detail =  models.CharField(max_length=30)
    username =  models.CharField(max_length=30)
    password2 =  models.CharField(max_length=30)
    num =  models.CharField(max_length=30)
    note =  models.CharField(max_length=30)


    def __str__(self):
        return str (self.id)