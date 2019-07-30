import requests,os

formdata = {
    "symbol":"SH600198", 			#代码
    "period":"5day",				#间隔时间
    "type":"before",				#类型
    "begin":"1510126200000",		#开始时间戳
    "end":"",						#结束时间戳
    "_":"",
}


url = "https://xueqiu.com/stock/forchartk/stocklist.json?"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

response = requests.get("https://xueqiu.com", headers=headers)

cookiejar = response.cookies

#转换字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

Cookie = ""
headers2 ={}

#多条cookies处理成字符串
for k,v in cookiedict.items():
	Cookie = k + "=" + v + ";" + Cookie

headers2["Cookie"] = Cookie
for k,v in headers.items():
	headers2[k] = v


print(headers2)
response = requests.post(url ,data = formdata, headers = headers2)
print (response.text)