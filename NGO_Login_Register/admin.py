# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import NGODetails ,NGO
from django.contrib import admin

# Register your models here.
class NGODetailsAdmin(admin.ModelAdmin):
    list_display = ["ngo_name",'location','contact',"ngo_item"]

    def ngo_name(self,obj):
        return obj.name.name

    def ngo_item(self,obj):
        return obj.item.item    

admin.site.register(NGODetails,NGODetailsAdmin)    
admin.site.register(NGO)