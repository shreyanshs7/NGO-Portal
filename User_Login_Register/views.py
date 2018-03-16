# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import jwt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from NGO_Portal.settings import SECRET_KEY
from .models import UserDetail
# Create your views here.

@csrf_exempt
def register(request):
    data = {}
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        aadhar = request.POST.get("aadhar")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            data['success'] = True
            data['message'] = "Username already exists"

            return JsonResponse(data,safe=False)
        else:
            userDetail = UserDetail.objects.create(
                name=name,
                username=username,
                mobile=mobile,
                aadhar=aadhar
            )
            userDetail.save()

            user = User.objects.create_user(
                username=username,
                password=password
            )    

            user.save()

            authKey = "176332A81pH4L759c8aad6"
            senderId = "CodeSVS"
            otp = random.randint(2000,9999)

            try:
                sendOtpUrl = "https://control.msg91.com/api/sendotp.php?authkey="+authKey+"&mobile=91"+str(mobile)+"&message=Your%20otp%20is%20"+str(otp)+"&sender="+senderId+"&otp="+str(otp)+""

                response = urllib2.urlopen(sendOtpUrl).read()
            
            except Exception as e:
                print(str(e))
                data['success'] = False
                data['message'] = "Otp not sent"

                return JsonResponse(data,safe=False)    
            
            
            jwtToken = {}
            jwtToken['username'] = username
            jwtToken['name'] = password
            jwtToken['mobile'] = mobile

            token = jwt.encode(jwtToken , SECRET_KEY , algorithm='HS256')

            data['success'] = True
            data['message'] = "User Registered"

            return JsonResponse(data,safe=False)
    else:
        data['success'] = False
        data['message'] = "Method not allowed"        

        return JsonResponse(data,safe=False)


@csrf_exempt
def login(request):
    data = {}
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print(str(e))
            data['success'] = False
            data['message'] = "Invalid Username"

            return JsonResponse(data,safe=False)    

        if user.check_password(password):

            jwtToken = {}
            jwtToken['username'] = username
            jwtToken['name'] = password
            jwtToken['mobile'] = mobile

            token = jwt.encode(jwtToken , SECRET_KEY , algorithm='HS256')

            data['success'] = True
            data['message'] = "User authenticated"
            data['token'] = token

            return JsonResponse(data,safe=False)

        else:

            data['success'] = False
            data['message'] = "Invaild credentials"    

            return JsonResponse(data,safe=False)

