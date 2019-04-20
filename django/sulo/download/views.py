from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .import models
from functools import wraps
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'file.html')