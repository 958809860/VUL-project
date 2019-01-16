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
                if i.find(string)!=-1:
                        print (filename)
 
 
def get_process_files(root_dir):
    cur_dir=os.path.abspath(root_dir)
    file_list=os.listdir(cur_dir)
    process_list=[]
    picture_list=[]
    for file in file_list:
        fullfile=cur_dir+"\\"+file
        if os.path.isfile(fullfile):
            if endWith(fullfile,'.json','.txt','.ts') ==True:
                process_list.append(fullfile)
            if endWith(fullfile,'.png','.jpg') ==True:
                picture_list.append(fullfile)
        elif os.path.isdir(fullfile):
            dir_extra_list=get_process_files(fullfile)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    process_list.append(x)
    return process_list,picture_list
 
def count_files(root_dir,string):
        temp=get_process_files(root_dir)
        process_list=temp[0]
        picture_list=temp[1]
        print(process_list)
        print(picture_list)
        
        for files in process_list:
            search_string(files,string)
 
 
if __name__=='__main__':
        root_dir=r'E:\gitclone\VUL-project\Rename\icon'#目录
        string='scard_76'#要搜索的字符串
        count_files(root_dir,string)
