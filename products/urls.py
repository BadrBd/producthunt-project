from django.contrib import admin
from django.urls import path, include
from .views import Home, ProductCreateView


app_name="products"
urlpatterns = [
    path('', Home, name='home'),
    path('create/', ProductCreateView, name='product-create'),

 
]