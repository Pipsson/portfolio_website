from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Portfolio (models.Model):
    image = models.ImageField()
    name = models.CharField(max_length= 200, default= 'biteschool')
    discription = models.TextField(max_length= 300)
    link1 = models.URLField( blank= True)
    link2 = models.URLField(blank= True)

    def __str__(self):
           return self.name
    