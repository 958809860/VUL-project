from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('laojin0.txt', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="laojin0.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('laojin1.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="laojin1.txt"'
msg.attach(att2)

#加邮件头
msg['to'] = '2661451986@qq.com'
msg['from'] = '958809860@qq.com'
msg['subject'] = '老金'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.qq.com')
    server.login('958809860@qq.com','授权码')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print ('发送成功')
except Exception as e:
    print(str(e))