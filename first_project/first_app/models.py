from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
  title=models.CharField(max_length=100)
  slug=models.SlugField()
  body=models.TextField()
  date=models.DateTimeField(auto_now_add=True)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

def __str__(self):
    return self.title

def snippet(self):
    return self.body[:50]+'...'
def __str__(self):
    return self.username