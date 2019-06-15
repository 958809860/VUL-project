from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .import models
from functools import wraps
from itertools import chain
# Create your views here.
def index(request):
    result1 = []
    result2 = []
    all = len(models.product.objects.all())
    for i in range(all):
        productList = models.product.objects.filter(product_id = i+1).values('product_id','name','desc')
        productLink = models.downloadlink.objects.filter(product_id= productList[0]['product_id']).values('id','product_id','product_link')
        result1.append(productList)
        result2.append(productLink)
    print (result1,result2)
    return render(request, 'sulo-support.html',{'result1': result1,'result2': result2})