from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Questions
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login/')
def index(request):
    htmlCode = '<table border="1px">'
    for row in Questions.objects.all():
        htmlCode += ('<tr><td>' + str(row.id) + '<td><td>' + row.questionConttent + '<td><td>' + row.answer + '<td>') 
    htmlCode += '</table>'
    return HttpResponse(htmlCode) 

def login(request):

    try:
        userName = request.POST['usr']
        userPwd = request.POST['pwd']
        user = auth.authenticate(username = userName,password = userPwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/check/')
        else:
            return render(request,'login.html',{'msg':'用户名或密码不正确'})
    except:
        return render(request,'login.html',{'msg':None})