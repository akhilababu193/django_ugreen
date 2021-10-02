from django.db import models


# Create your models here.
class ug_new_arrivals(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class ug_best_seller(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    hot = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)

class ug_blogs(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    heading = models.TextField()

