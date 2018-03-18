# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Donation
from django.contrib import admin

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ['get_user','get_item','quantity','date','time','accepted']

    def get_user(self,obj):
        return obj.user.name

    def get_item(self,obj):
        return obj.item.item

admin.site.register(Donation,DonationAdmin)    
