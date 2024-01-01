from typing import Any
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db.models.signals import post_save


class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)   #USED AS A FOREIGN KEY TO EXTEND USER
    phone = PhoneNumberField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
  
    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Account(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)
   

class Listing(models.Model):

    CITY_CHOICES= [
        
        ("Karachi", "Karachi"),
        ("Lahore", "Lahore"),
        ("Islamabad", "Islamabad"),
        ("Faisalabad", "Faisalabad"),
        ("Hyderabad", "Hyderabad"),
        ("Peshawar", "Peshawar"),
        ("Quetta", "Quetta"),
        ("Rawalpindi", "Rawalpindi"),
        ("Multan", "Multan"),
        ("Gujranwala", "Gujranwala"),
    ]

    PURPOSE_CHOICES= [
        ("Sell", "Sell"),
        ("Rent", "Rent"),
    ]
    
    PROPERTY_CHOICES= [
        ("House", "House"),
        ("Flat", "Flat"),
        ("Portion", "Portion"),
        ("Room", "Room"),
        ("Penthouse", "Penthouse"),
        ("Farm House", "Farm House"),
    ]

    BED_CHOICES= [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7+", "7+"),

    ]

    BATH_CHOICES= [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7+", "7+"),
    ]

    AREA_CHOICES= [
            ("40", "40"),
            ("50", "50"),
            ("60", "60"),
            ("70", "70"),
            ("80", "80"),
            ("90", "90"),
            ("100", "100"),
            ("120", "120"),
            ("150", "150"),
            ("200", "200"),
            ("220", "220"),
            ("250", "250"),
            ("300", "300"),
            ("350", "350"),
            ("400", "400"),
            ("420", "420"),
            ("450", "450"),
            ("500+", "500+"),


        ]
 
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)   #Many listing can be done by one user, Many to One
    title= models.CharField(max_length=150, null=True)
    purpose = models.CharField(max_length=150, null=True, choices=PURPOSE_CHOICES)
    property_type=models.CharField(max_length=150, null=True, choices=PROPERTY_CHOICES)
    num_bedrooms = models.CharField(max_length=2,null=True, choices=BED_CHOICES)
    num_bathrooms = models.CharField(max_length=2,null=True, choices=BATH_CHOICES)
    area_size = models.CharField(max_length=10,null=True, choices=AREA_CHOICES)
    city=models.CharField(max_length=150, null=True, choices=CITY_CHOICES)
    location = models.CharField(max_length=150, null=True)
    plot_number=models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True)
    mobile_num = PhoneNumberField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    map_link = models.URLField(null=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    image_4 = models.ImageField(null=True, blank=True)
    image_5 = models.ImageField(null=True, blank=True)

    
    def get_absolute_url(self):
        return reverse('retrieve', args=[str(self.pk)])


    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)   
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)   
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']