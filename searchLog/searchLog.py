# -*- coding: utf-8 -*-
import os
import re
import sys

#根据文件扩展名判断文件类型
def endWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

#在读取行时判断是否存在检索字符串
def searchstring(each_line):    
        for i in range(len(stringlist)):
                if each_line.find(stringlist[i]) != -1:
                        pass
                else:
                        return False

#获取路径下所有.lua（可添加其他格式）文件的路径
def get_process_files(root_dir):
        file_list = []
        for root, dirs, files in os.walk(root_dir, topdown=False):
                for name in files:
                        if endWith(name,'.lua','py') ==True:
                        #print('存在的文件：\n',os.path.join(root, name))#文件
                                file_list.append(os.path.join(root, name))
                # for name in dirs:
                        # print('存在的文件夹：\n'os.path.join(root, name))#文件夹
                        # pass
        return file_list

#如果检索到字符串则打印行数及内容
def findstring(file):
        document = open(file, 'r+', encoding = 'utf-8')
        count = 0
        for each_line in document:
                count += 1 
                if searchstring(each_line) != False:
                        try:
                                print(file,":",count,":",each_line)
                        except BaseException as e:
                                print(e)
        document.close()

if __name__=='__main__':
        stringlist = sys.argv[1:]
        root_dir = r"E:\gitclone\VUL-project"
        file_list = get_process_files(root_dir)
        # print(file_list)
        for i in file_list:
                findstring(i)