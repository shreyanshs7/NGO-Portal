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
import random
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
    if request.method == "POST":

        posted = {}
        posted['key'] = "rjQUPktU"
        posted['txnid'] = request.POST.get("id")
        posted['productinfo'] = "donation"
        posted['firstname'] = request.POST.get('firstname')
        posted['email'] = request.POST.get('email')
        posted['amount'] = request.POST.get('amount')

        salt="e5iIg1jwi8"

        hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"

        hashString =''
        hashVarsSeq=hashSequence.split('|')
        print(hashVarsSeq)
        for i in hashVarsSeq:
            try:
                hashString+=str(posted[i])
            except Exception:
                hashString+=''
            hashString+='|'
        hashString+=salt    
        print(hashString)
        hash = hashlib.sha512(hashString).hexdigest().lower()
        print(hash)

        baseUrl = ""

        posted['hash'] = hash
        posted['surl'] = baseUrl+"/success"
        posted['furl'] = baseUrl+"/failure"
        posted['service_provider'] = "payu_paisa"

        return JsonResponse(posted,safe=False)

@csrf_exempt
def success(request):
    
    amount = request.POST.get('amount')
    id = request.POST.get('txnid')
    ngoObj = NGO.objects.get(id=id)
    ngoObj.fund += amount
    ngoObj.save()

    data = {}
    data['success'] = True
    data['message'] = "Payment done" 

    return JsonResponse(data,safe=False)

@csrf_exempt
def failure(request):
    data = {}
    data['success'] = False
    data['message'] = "Payment failed"

    return JsonResponse(data,safe=False)






