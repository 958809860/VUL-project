import os
import time
path = r"QQScLauncher.exe"
while True:
    try:
        cmd = r'start ' + path
        print(cmd)
        os.system(cmd)
        time.sleep(20)#  5S间隔关闭进程 TIM.exe
        os.system('taskkill /f /im TIM.exe') #结束TIM.exe进程
        time.sleep(10)#  5S间隔开启进程 TIM.exe
    except BaseException as e:
        print (e)