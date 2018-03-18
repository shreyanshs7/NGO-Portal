from django.conf.urls import url,include
from django.contrib import admin
from .views import NgoApi

urlpatterns = [
    url(r'^api', NgoApi , name="ngoApi"),
]