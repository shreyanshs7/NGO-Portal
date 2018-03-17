# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
import jwt
from NGO_Portal.settings import SECRET_KEY
from NGO_Items.models import Item
from NGO_Login_Register.models import NGODetails
from User_Login_Register.models import UserDetail
from .models import Donation
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def createDonation(request):
    data = {}
    if request.method == "POST":
        ngo = request.POST.get("ngoId")
        item = request.POST.get('itemId')
        quantity = request.POST.get('quantity')
        details = request.POST.get('details')
        token = request.POST.get('token')

        jwtData = jwt.decode(token , SECRET_KEY , algorithm=['HS256'])

        username = jwtData['username']

        try:
            userObj = UserDetail.objects.get(username=username)
            itemObj = Item.objects.get(id=item)
            ngoObj = NGODetails.objects.get(id=ngo)
        except UserDetail.DoesNotExist:
            data['success'] = False
            data['message'] = "Invalid username"
        except Item.DoesNotExist:
            data['success'] = False
            data['message'] = "Invalid item"
        except NGODetails.DoesNotExist:
            data['success'] = False
            data['message'] = "Invalid NGO detail"    
            
            return JsonResponse(data,safe=False)

        donationObj = Donation.objects.create(
            user=userObj,
            item=itemObj,
            quantity=quantity,
            details=details
        )

        donationObj.save()

        data['success'] = True
        data['message'] = "Donation done successfully"

        return JsonResponse(data,safe=False)
    else:
        data['success'] = False
        data['message'] = "Method not allowed"

        return JsonResponse(data,safe=False)


@csrf_exempt
def pay(request):
    pass