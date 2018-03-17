from django.conf.urls import url,include
from django.contrib import admin
from .views import createDonation

urlpatterns = [
    url(r'^create', createDonation , name="createDonation"),
]