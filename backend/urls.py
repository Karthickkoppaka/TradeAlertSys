from django.urls.conf import include
from django.urls import path
from .fyers import urls as furls


urlpatterns = [
    #Login Fyers Session
    path('Fyers/',include(furls)),
]