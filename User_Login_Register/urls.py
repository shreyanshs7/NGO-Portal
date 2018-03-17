from django.conf.urls import url
from django.contrib import admin
from .views import register , login ,verifyOtp

urlpatterns = [
    url(r'^register/', register , name="register"),
    url(r'^login/', login , name="login"),
    url(r'^verify/', verifyOtp , name="verifyOtp")
]

