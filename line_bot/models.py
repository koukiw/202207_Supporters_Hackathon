from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200,blank=True,null=True)
    image = models.CharField(max_length=200,blank=True,null=True)
    category = models.CharField(max_length=200,default = "NoCategory")
    detail = models.CharField(max_length=200,default = "NoCategory")

class Category(models.Model):
    category = models.CharField(max_length=200,default = "NoCategory")


class Status(models.Model):
    place_id = models.IntegerField(blank=True,null=True)
    status = models.IntegerField()