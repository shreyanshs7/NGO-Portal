# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Item
from django.contrib import admin

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','item']
    
admin.site.register(Item,ItemAdmin)    