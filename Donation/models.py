# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from User_Login_Register.models import UserDetail
from django.db import models
from NGO_Items.models import Item
# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey("User_Login_Register.Userdetail")
    item = models.ForeignKey("NGO_Items.Item")
    quantity = models.IntegerField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    details = models.CharField(max_length=1000)