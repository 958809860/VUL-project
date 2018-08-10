## -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import xlrd
import random
browser = webdriver.Chrome(r"chromedriver.exe")
file = r"WebHttp.xls"
document = xlrd.open_workbook(file)  # 打开文件
sheet1 = document.sheet_by_index(0)  # 通过索引获取表格
eachlink = {}
nrows = sheet1.nrows
ncols = sheet1.ncols
print(nrows, ncols)
for x in range(1,nrows):  #公司脚本，后边会加字符串
    eachlink[x] = sheet1.cell_value(x, 2)+'JX'
    print(int(sheet1.cell_value(x, 0)),sheet1.cell_value(x, 1))

num = input('请输入打开网页个数：\n')
link = input('请选择要打开的网页：\n')
count = 0
random_num = random.randint(100000, 999999)
while count < int(num):
    js = "window.open('" + eachlink[int(link)] + str(random_num+count) + "');"
    browser.execute_script(js)
    count += 1
while True:
    command = input("1：刷新，2：清除缓存并刷新,3:退出\n")
    if command == '3':
        browser.quit()
        break
    elif command == '1':
        handles = browser.window_handles
        for x in range(1,len(handles)):
            browser.switch_to_window(handles[x])
            browser.refresh()
        browser.switch_to_window(handles[1])
    elif command =='2':
        cookies = browser.get_cookies()
        print(f"main: cookies = {cookies}")
        browser.delete_all_cookies()