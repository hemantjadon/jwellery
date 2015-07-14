from django.shortcuts import render,redirect
from Products.models import *
from roughViews.forms import filterForm
from django.http import HttpResponse
from django.core import serializers

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
	print(request.GET['filter'])
	return render(request,'jwelleryProductPage/jewlleryProductPage.html',{"page":"jwellery","filterForm":filterForm})