from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Resume/index.html")

def philani(request):
    return HttpResponse("Hello Philani")

def lungas(request):
    return HttpResponse("Hello Lungas")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "Resume/greet.html", {
        "name": name.capitalize()
    })