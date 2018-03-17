# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from NGO_Login_Register.models import NGODetails ,NGO
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

    id = request.GET.get("id")
    
    itemsObj = Item.objects.filter(id=id)

    NGOObj = NGODetails.objects.filter(item=itemsObj)

    print(NGOObj)    

    NGOList = []

    for obj in NGOObj:
        ngoName = NGO.objects.get(name=obj.name)
        tempData = {
            "id": obj.id,
            "name": ngoName.name,
            "location" : obj.location,
            "contact" : obj.contact
        }    

        NGOList.append(tempData)
        tempData = {}

    print(NGOList)

    data = {}
    data['success'] = True
    data['ngo'] = NGOList

    return JsonResponse(data,safe=False)    