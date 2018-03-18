from django.conf.urls import url,include
from django.contrib import admin
from .views import createDonation ,pay , success , failure , donationApi,accept

urlpatterns = [
    url(r'^create', createDonation , name="createDonation"),
    url(r'^pay', pay , name="pay"),
    url(r'^success', success , name="success"),
    url(r'^failure', failure , name="failure"),
    url(r'^api', donationApi , name="api"),
    url(r'^accept', accept , name="accept"),
     
]