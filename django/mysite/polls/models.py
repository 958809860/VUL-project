from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class userinfo(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()

class message(models.Model):
    username = models.CharField(max_length=20,null=False)
    password = models.CharField(max_length=15,null=False)

class addmessage(models.Model):
    username = models.CharField(max_length=50,null=False)
    project = models.CharField(max_length=50,null=False)
    desc = models.CharField(max_length=50,null=False)
    estimatedTime = models.IntegerField(null=False)
    remainingTime = models.IntegerField(null=False)
    remark = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)