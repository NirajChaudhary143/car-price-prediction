from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(null=True)

class contactList(models.Model):
    icon=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    address=models.TextField()