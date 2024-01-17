from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=220)
    email=models.CharField( max_length=220)
    phone=models.CharField( max_length=12)
    issue=models.TextField()
    date=models.DateField()
     