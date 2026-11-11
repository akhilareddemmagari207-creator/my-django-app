from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional fields
    age = models.PositiveBigIntegerField()
    phone = models.BigIntegerField()
    house_no = models.IntegerField()
    landmark = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    userimg = models.ImageField(upload_to='userpic/',blank=True,null=True)
class LoginForm(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class vendorRegistration(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    travels_name=models.CharField(max_length=100)
    gst_no=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    address_1=models.CharField(max_length=100)
    address_2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField(max_length=100)
    licence_no=models.IntegerField()
    licence_img=models.ImageField(upload_to='licence_img/',blank=True,null=True)
    travel_img=models.ImageField(upload_to='travel_img/',blank=True,null=True)
    estd_year=models.IntegerField()
    is_approved=models.BooleanField(default=False)

