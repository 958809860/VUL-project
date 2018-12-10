from aip import AipSpeech

APP_ID = '******'
API_KEY = '************'
SECRET_KEY = '***************'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

txt = '老金哈哈'

result  = client.synthesis(txt, 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('txt.mp3', 'wb') as f:
        f.write(result)