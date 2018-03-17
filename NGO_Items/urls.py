from django.conf.urls import url,include
from django.contrib import admin
from .views import ItemsApi , NGOApi

urlpatterns = [
    url(r'^api/items', ItemsApi , name="itemApi"),
    url(r'^api/ngo', NGOApi , name="ngoApi"),
]