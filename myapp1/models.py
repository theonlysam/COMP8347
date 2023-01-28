import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    type = models.ForeignKey(Type, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)

class Client(User):
    CITY_CHOICES = [
        ("WD","Windsor"),
        ("TO", "Toronto"),
        ("CH", "Chatham"),
        ("WL", "WATERLOO"),
    ]
    fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES,default="WD")
    interested_in = models.ManyToManyField(Type)



