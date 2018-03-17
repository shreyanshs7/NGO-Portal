from django.conf.urls import url,include
from django.contrib import admin
from .views import createDonation ,pay , success , failure

urlpatterns = [
    url(r'^create', createDonation , name="createDonation"),
     url(r'^pay', pay , name="pay"),
     url(r'^success', success , name="success"),
     url(r'^failure', failure , name="failure"),
]