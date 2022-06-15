import imp
import os
import datetime
from venv import create
from django.db import models
import PIL
from PIL import Image
from django.contrib.auth.models import User

#--------------------user profile related imports
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save



# Create your models here.
def get_file_path(request, filename):
     original_filename = filename
     now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
     filename = '%s%s' % (now_time, original_filename)
     return os.path.join('uploads/', filename)



class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image= models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length = None)
    description = models.TextField(max_length=500, name=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    
class Size(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    size_type = models.CharField(max_length=150, null=False, blank=False)
    image= models.ImageField(upload_to= get_file_path, height_field=None, width_field=None, max_length = None)
    description = models.TextField(max_length=500, name=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.size_type



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image= models.ImageField(upload_to= get_file_path, height_field=None, width_field=None, max_length = None)
    brief_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, name=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    clearance_sale = models.BooleanField(default=False, help_text='0=default, 1=Clearance')
    new_arrival = models.BooleanField(default=False, help_text='0=default, 1=New Arrival')
    viewed_on_homepage = models.BooleanField(default=False, help_text='0=default, 1=Homepage')
    meta_title = models.CharField(max_length=150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



# --------------------------profile model----------------------------


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mycart = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return self.user.username

#-------------------------signal showing a profile associated to a user once they sign up-------------------


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)



# -----------------------------------------------------cart model---------------------------------------------


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
