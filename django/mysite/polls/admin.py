from django.contrib import admin
from polls.models import message
from polls.models import addmessage
# Register your models here.
class messageList(admin.ModelAdmin):
    list_display = ('id','username', 'password') # list
admin.site.register(message, messageList)

class addmessageList(admin.ModelAdmin):
    list_display = ('id', 'username', 'project', 'desc', 'estimatedTime', 'remainingTime', 'remark')
admin.site.register(addmessage, addmessageList)


