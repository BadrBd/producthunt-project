from django.contrib import admin
from django.urls import path, include
from .views import Home, ProductCreateView, ProductDetailView, Upvote


app_name="products"
urlpatterns = [
    path('', Home, name='home'),
    path('create/', ProductCreateView, name='product-create'),
    path('detail/<int:product_id>/', ProductDetailView, name='product-detail'),
    path('detail/<int:product_id>/', ProductDetailView, name='product-detail'),
    path('upvote/<int:product_id>/', Upvote, name='upvote'),


 
]