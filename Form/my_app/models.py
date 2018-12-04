# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name
