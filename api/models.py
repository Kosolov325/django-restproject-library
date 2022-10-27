from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  livros = models.ManyToManyField('Livro', blank=True)


class Livro(models.Model):
    title = models.CharField(max_length=200, blank=True, default="")
    author = models.CharField(max_length=200, blank=True, default="")
    data = models.DateField(blank=True, default='0000-00-00')
    
    def __str__(self):
       return self.title
    

