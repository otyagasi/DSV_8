from django.shortcuts import render
from django.http.response import HttpResponse
import random
# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")
def index(request):
    params = {"text": "Hello, World!"
              , "number": random.randint(1, 100)}
    return render(request, "hello/index.html", params)
def myprofile(request):
    params = {} 
    return render(request, "hello/myprofile.html", params)