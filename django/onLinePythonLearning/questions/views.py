from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions

# Create your views here.
def index(request):
    htmlCode = '<table border="1px">'
    for row in Questions.objects.all():
        htmlCode += ('<tr><td>' + str(row.id) + '<td><td>' + row.questionConttent + '<td><td>' + row.answer + '<td>') 
    htmlCode += '</table>'
    return HttpResponse(htmlCode) 