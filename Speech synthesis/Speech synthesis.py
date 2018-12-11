import os
from aip import AipSpeech

APP_ID = '*********'
API_KEY = '************'
SECRET_KEY = '*************'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

TXT = r'./eg.txt'
document = open(TXT, 'r+')

def speech(txt,line):
    result  = client.synthesis(txt, 'zh', 1, {
        'vol': 5,
    })
    name = str(line) + '.mp3'
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(name, 'wb') as f:
            f.write(result)

def readDocument():
    account = 0
    for each_line in document:
        account += 1
        x = speech(each_line,account)

        print(x)
readDocument()