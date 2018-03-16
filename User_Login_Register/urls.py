from django.conf.urls import url
from django.contrib import admin
from .views import register , login

urlpatterns = [
    url(r'^register/', register , name="register"),
    url(r'^login/', login , name="login"),
]

