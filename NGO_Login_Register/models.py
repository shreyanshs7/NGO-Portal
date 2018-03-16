# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from NGO_Items.models import Item
from django.db import models

# Create your models here.
class NGODetails(models.Model):
    name = models.CharField(max_length=50)
    item = models.ForeignKey('NGO_Items.Item')
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=10)
    fund = models.IntegerField(default=1000)