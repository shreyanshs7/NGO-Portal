from django.conf.urls import url,include
from django.contrib import admin
from .views import createDonation ,pay

urlpatterns = [
    url(r'^create', createDonation , name="createDonation"),
     url(r'^pay', pay , name="pay"),
]