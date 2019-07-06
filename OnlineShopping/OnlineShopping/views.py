from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homePage.html')
def login(request):
    return render(request,'login.html')
def product(request):
    return render(request,'product.html')
def register(request):
    return render(request,'register.html')
def order(request):
    return render(request,'order.html')
def feedback(request):
    return render(request,'feedback.html')
