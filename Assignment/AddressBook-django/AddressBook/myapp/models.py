from django.db import models
from django.db.models.fields import CharField
import datetime

# Create your models here.
class Address_Book(models.Model):

    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    DOB = models.DateField(default=datetime.date.today)
    Address = models.TextField()
    Pincode = models.TextField(max_length=255)
