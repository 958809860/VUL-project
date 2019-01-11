#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

path = r'C:/Users/VULCAN/Desktop/icon/' #要批量修改的文件路径

rename = os.listdir(path)

def rename_replace(old,new,temp):
    new_name = temp.replace(old,new,1)
    return new_name

def rename_prefix(prefix,temp):
    new_name = prefix + temp
    return new_name

def rename_suffix(temp,suffix):
    new_name = temp.split('.',1)[0] + suffix + '.' +temp.split('.',1)[1]
    return new_name


def run():
    for temp in rename:
        # newname = rename_replace('old','new',temp)      #替换某些内容 old new
        # newname =  rename_prefix('前缀',temp)        #加前缀
        # newname =  rename_suffix(temp,'后缀')        #加后缀
        print (newname)
        os.rename( path + temp, path + newname)

run()