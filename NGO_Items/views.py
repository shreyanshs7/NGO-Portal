# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from NGO_Login_Register.models import NGODetails
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


def NGOApi(request):

    NGOObj = NGODetails.objects.all()

    NGOList = []

    for obj in NGOObj:

        tempData = {
            "id": obj.id,
            "name": obj.name,
            "location" : obj.location,
            "contact" : obj.contact
        }    

        NGOList.append(tempData)
        tempData = {}

    data = {}
    data['success'] = True
    data['ngo'] = NGOList

    return JsonResponse(data,safe=False)    