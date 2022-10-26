from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    contact=models.CharField(max_length=11)
    email=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
