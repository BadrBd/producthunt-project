
from django.contrib import admin
from django.urls import path, include
from .views import Login, Signup, Logout

app_name="accounts"
urlpatterns = [
	path('login/', Login, name='login'),
	path('signup/', Signup, name='signup'),
	path('logout/', Logout, name='logout'),
]