# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
# Create your views here.

def ItemsApi(request):

    itemsObj = Item.objects.all()

    itemsList = []

    for obj in itemsObj:
        tempData = {
            "id" : obj.id,
            "item" : obj.item
        }
        itemsList.append(tempData)
        tempData = {}

    data = {}
    data['success'] = True
    data['items'] = itemsList

    return JsonResponse(data,safe=False)    