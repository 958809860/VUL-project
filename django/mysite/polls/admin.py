from django.contrib import admin
from polls.models import message
from polls.models import addmessage
# Register your models here.
admin.site.site_title="晨会日志管理"
admin.site.site_header="日志管理"
admin.site.index_title="日志管理"

class messageList(admin.ModelAdmin):
    list_display = ('id','username', 'password') # list
admin.site.register(message, messageList)

class addmessageList(admin.ModelAdmin):
    list_display = ('id', 'username', 'project', 'desc', 'estimatedTime', 'remainingTime', 'remark')
admin.site.register(addmessage, addmessageList)


