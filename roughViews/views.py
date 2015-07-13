from django.shortcuts import render,redirect
from Products.models import *
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def initialPage(request):
	return render(request,'initialPage/initialPageAccordian.html',{})

def jwelleryPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"jwellery"})