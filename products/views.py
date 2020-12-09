from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Product

# Create your views here.
def Home(request):
	return render(request,'products/home.html')

@login_required
def ProductCreateView(request):
	if request.method=='POST':
		if request.POST["title"] and request.POST["body"] and request.POST["url"] and request.FILES["icon"] and request.FILES["image"]:
			product = Product()
			product.title = request.POST["title"]
			product.body = request.POST["body"]

			if request.POST["url"].startswith('http://') or request.POST["url"].startswith('https://'):
				product.url = request.POST["url"]

			else:
				product.url = 'http://' + request.POST["url"]
			
			product.icon = request.FILES["icon"]
			product.image = request.FILES["image"]
			product.pub_date= timezone.datetime.now()
			product.hunter=request.user
			product.save()
			return HttpResponseRedirect(reverse('products:home'))

		else:
			return render(request,'products/product_create.html', {'error': 'All the fields are required'})
		

	return render(request,'products/product_create.html')
