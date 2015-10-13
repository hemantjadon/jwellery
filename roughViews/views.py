from django.shortcuts import render,redirect
from Products.models import *
from roughViews.forms import filterForm
from django.http import HttpResponse
from django.core import serializers
from django.apps import apps

# Create your views here.
def initialPage(request):
	return render(request,'initialPage/initialPageAccordian.html',{})

def jwelleryPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"jwellery"})

def solitaresPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"solitares"})

def goldCoinsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"goldCoins"})

def collectionsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"collections"})

def giftsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"gifts"})

def productPage(request):
	identifier=request.GET.getlist('identifier')
	products=[]
	if ((len(identifier) is not 0) and (identifier[0] is not '')):
		app=apps.get_app_config('Products')
		models=app.get_model(identifier[0])
		print(models)
		products+=models.objects.all()

	return render(request,'jwelleryProductPage/jewlleryProductPage.html',{"page":"jwellery","filterForm":filterForm,"products":products})

def product_detail_page(request):
	return render(request,'product_detail/product_detail.html',{})
