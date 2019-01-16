#!/usr/bin/python
#-*- coding: utf-8 -*-

import os,sys

#根据文件扩展名判断文件类型
def endWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def search_string(filename,string):
    with open(filename,'r+',encoding = 'utf-8') as file:
            lines=file.readlines()
    file.close()

    for i in lines:
        i=i.strip()
        if i.find(string) != -1:
            print (filename,string)
            return string

def get_process_files(root_dir):

    file_list = []
    process_list=[]
    picture_list=[]

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))#文件
            file_list.append(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))#文件夹

    for file in file_list:
        if os.path.isfile(file):
            if endWith(file,'.json','.txt','.ts') ==True:
                process_list.append(file)
            if endWith(file,'.png','.jpg') ==True:
                picture_list.append(file)
        elif os.path.isdir(file):
            dir_extra_list=get_process_files(file)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    process_list.append(x)
    return process_list,picture_list
 
def count_files(root_dir):
        temp=get_process_files(root_dir)
        process_list=temp[0]
        picture_list=temp[1]
        #print('\n\nprocess_list=',process_list,'\n\npicture_list=',picture_list)
        for num in range(len(picture_list)):
            string = os.path.basename(picture_list[num]).split('.',1)[0]
            for files in process_list:
                #print(files,string)
                if search_string(files,string) != string:
                    if os.path.exists(picture_list[num]):
                        os.remove(picture_list[num])
                        print('deleted',picture_list[num],string)
 
if __name__=='__main__':
    root_dir=r'E:\gitclone\VUL-project\Rename'#目录
    count_files(root_dir)
