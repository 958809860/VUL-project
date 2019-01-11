#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

path = r'C:/Users/VULCAN/Desktop/icon/' #要批量修改的文件路径

rename = os.listdir(path)

def rename_replace():
    for temp in rename:
        new_name = temp.replace('81','80',1)  #输入替换前内容，替换后内容
        print (new_name)
        os.rename(path+temp,path+new_name)

rename_replace()
