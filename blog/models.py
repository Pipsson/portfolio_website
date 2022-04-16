from email.mime import image
from django.db import models

# Create your models here.
class Portfolio (models.Model):
    image = models.ImageField()
    discription = models.TextField(max_length= 300)
    link1 = models.URLField( blank= True)
    link2 = models.URLField(blank= True)
