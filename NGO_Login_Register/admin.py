# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import NGODetails
from django.contrib import admin

# Register your models here.
class NGODetailsAdmin(admin.ModelAdmin):
    list_display = ['name','location','contact','fund']

admin.site.register(NGODetails,NGODetailsAdmin)    
