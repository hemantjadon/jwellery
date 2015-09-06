from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def LoginSignup(request):
    print(request.is_ajax())
    return render(request,'login-signup/login-signup.html',{})
