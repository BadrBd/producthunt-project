from django.contrib import admin
from django.urls import path, include
from .views import Home


app_name="products"
urlpatterns = [
    path('', Home, name='home'),

 
]