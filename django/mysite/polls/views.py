from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .import models
from functools import wraps
# Create your views here.

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/login/')
    return inner

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        print(user,pwd)
        try:
            getpwd = models.message.objects.get(username = user).password
            print(getpwd)
            if str(getpwd) == str(pwd):
                request.session['is_login']='1' 
                request.session['username']=user
                return redirect('/addmessage/')
        except BaseException:
            error_msg = "用户名或密码错误"   
    return render(request,'login.html', {'error_msg': error_msg})

def addmoringlog(request):
    pass

@check_login
def addmessage(request):
    username = request.session.get('username')
    if request.method == "POST":
        project = request.POST.get('project',None)
        desc = request.POST.get('desc', None)
        estimatedTime = request.POST.get('estimatedTime', None)
        remainingTime = request.POST.get('remainingTime', None)
        remark = request.POST.get('remark', None)
        twz = models.addmessage.objects.create(username=username, project=project, desc=desc, estimatedTime=estimatedTime, remainingTime=remainingTime, remark=remark) #t提交内容进行数据库写入
        twz.save()
    return render(request,'addmessage.html',{'username': username})