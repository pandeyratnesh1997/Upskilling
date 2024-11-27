from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Welcome to about page")

def contact(request):
    return HttpResponse("Welcome to contact page")