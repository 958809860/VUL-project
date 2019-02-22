from django.db import models

# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key = True)
    questionConttent = models.CharField(max_length = 200,unique = True)
    answer = models.CharField(max_length = 50)

class Department(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    def _str_ (self):
        return self.name

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField('登录账号',max_length = 50,unique = True)
    password = models.CharField('密码',max_length = 100)
    number = models.CharField('学号',max_length = 50,unique = True)
    name = models.CharField('姓名',max_length = 8)
    sex = models.CharField('性别',max_length = 1)
    email = models.EmailField('电子邮箱')
    gradeClass = models.CharField('年级班级',max_length = 15)
    registerTime = models.DateTimeField('注册日期',auto_now = True)
