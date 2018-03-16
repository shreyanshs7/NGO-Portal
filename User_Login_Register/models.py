# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)