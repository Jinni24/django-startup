from email import message
from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Inquiry(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=32)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
