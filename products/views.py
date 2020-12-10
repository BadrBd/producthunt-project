from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Product

# Create your views here.
def Home(request):
	products = Product.objects.all()

	return render(request,'products/home.html', {'product_list':products})

@login_required(login_url="/accounts/signup")
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
			return HttpResponseRedirect('/detail/' + str(product.id))

		else:
			return render(request,'products/product_create.html', {'error': 'All the fields are required'})
		

	return render(request,'products/product_create.html')

@login_required
def ProductDetailView(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request,'products/product_detail.html',{'instance':product})

@login_required(login_url="/accounts/signup")
def Upvote(request, product_id):
	if request.method=='POST':

		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
	return HttpResponseRedirect('/detail/' + str(product.id))




