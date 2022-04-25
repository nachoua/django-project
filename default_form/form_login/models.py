from django.db import models
from django.db.models.fields import CharField

# Create your models hefre.
class Login(models.Model):
 usernam = models.CharField(max_length=100)
 password = models.CharField(max_length=50)
 
 def __str__(self):
    return self.usernam