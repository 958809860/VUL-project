from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .import models
from functools import wraps
# Create your views here.
def index(request):
    productList = models.product.objects.all().values('id','name','desc')
    # productLink = models.downloadlink.objects.get(id=productList.id)
    print (type(productList))
    # productList['link'] = productLink
    result = productList
    print (result)
    return render(request, 'file.html',{'result': result})