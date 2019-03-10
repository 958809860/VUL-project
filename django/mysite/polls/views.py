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
        log = request.POST.get('addlog',None)
        print(user,pwd,log)
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
    msg = ""
    username = request.session.get('username')
    if request.method == "POST":
        project = request.POST.get('project',None)
        desc = request.POST.get('desc', None)
        try:
            estimatedTime = int(request.POST.get('estimatedTime', None))
            remainingTime = int(request.POST.get('remainingTime', None))
            if project !=None and desc !=None and estimatedTime !=None and remainingTime !=None:
                remark = request.POST.get('remark', None)
                twz = models.addmessage.objects.create(username=username, project=project, desc=desc, estimatedTime=estimatedTime, remainingTime=remainingTime, remark=remark) #t提交内容进行数据库写入
                twz.save()
                msg = '提交成功'
            else:
                msg = '信息输入有误，请重新输入'
        except BaseException:
            msg = '信息输入有误，请重新输入'
    return render(request,'addmessage.html',{'username': username,'msg': msg})
@check_login
def addlogshow(request):
    username = request.session.get('username')
    result = models.addmessage.objects.filter(username=username)    #取出id和user列，并生成一个列表
    print(result)
    return render(request,'addlogshow.html',{'result': result})