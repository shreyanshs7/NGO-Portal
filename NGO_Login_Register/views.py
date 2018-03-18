# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import NGO
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def NgoApi(request):

    ngoObj = NGO.objects.all()

    ngoList = []

    for obj in ngoObj:
        tempData = {
            "id": obj.id,
            "name" : obj.name,
            "fund" : obj.fund
        }
        ngoList.append(tempData)
        tempData = {}

    data = {}
    data['success'] = True
    data['ngo'] = ngoList

    return JsonResponse(data,safe=False)    