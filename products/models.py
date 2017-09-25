# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Ec_User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        s = str(self.user_id) + "," + str(self.fullname) + "," + str(self.email) + "," + str(self.password)
        return s


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='product_images', default='default.png')
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5,decimal_places=0)

    def __str__(self):
        s = str(self.product_id) + "," + str(self.name) + "," + str(self.name) + "," + str(self.image_url) + "," + str(self.description) + "," + str(self.price)
        return s


class Ec_Admin(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        s = str(self.user_id) + "," + str(self.fullname) + "," + str(self.email) + "," + str(self.password)
        return s
