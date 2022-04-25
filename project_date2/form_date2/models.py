from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class First(models.Model):
 title = models.CharField(max_length=50)
 firstname = models.CharField(max_length=100)
 lastname = models.CharField(max_length=100)
 phone_number = models.CharField(max_length=12)
 date = models.DateField(auto_now_add=True)
 thumb = models.ImageField(default='default.png',blank=True) 

def __str__(self):
    return self.title