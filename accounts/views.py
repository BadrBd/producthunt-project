from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def Login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST["username"],password=request.POST["password"])
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect(reverse('products:home'))
		else: 
			return render(request,'accounts/login.html', {'error': 'Credentials are incorrect!'})



	else:
		return render(request,'accounts/login.html')

def Signup(request):
	if request.method=='POST':
		#if the user enter infos
		if request.POST["password1"] == request.POST["password2"]:
			try:
				user = User.objects.get(username=request.POST["username"])
				return render(request,'accounts/signup.html', {'error': 'Username taken!'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
				auth.login(request,user)
				return HttpResponseRedirect(reverse('products:home'))
		else:
			return render(request,'accounts/signup.html', {'error': 'Passwords not matching'})



	else:
		#if the user wans to register
		return render(request,'accounts/signup.html')

def Logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return HttpResponseRedirect(reverse('products:home'))

	return render(request,'accounts/signup.html')