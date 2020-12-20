from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ginger(request):
    return HttpResponse("Hello, ginger!")

def gayis(request):
    return HttpResponse("Hello, gayis!!")

def greet1(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })