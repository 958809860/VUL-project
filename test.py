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
    cur_dir=os.path.abspath(root_dir)
    file_list=os.listdir(cur_dir)
    #print (file_list)
    process_list=[]
    picture_list=[]
    picturename_list = []
    for file in file_list:
        fullfile=cur_dir+"\\"+file
        if os.path.isfile(fullfile):
            if endWith(fullfile,'.json','.txt','.ts') ==True:
                process_list.append(fullfile)
            if endWith(fullfile,'.png','.jpg') ==True:
                picture_list.append(fullfile)
                picturename_list.append(os.path.basename(fullfile).split('.',1)[0])
        elif os.path.isdir(fullfile):
            dir_extra_list=get_process_files(fullfile)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    process_list.append(x)
    return process_list,picture_list,picturename_list
 
def count_files(root_dir):
        temp=get_process_files(root_dir)
        process_list=temp[0]
        picture_list=temp[1]
        picturename_list=temp[2]
        #print('\n\nprocess_list=',process_list,'\n\npicture_list=',picture_list,'\n\npicturename_list=',picturename_list)
        for num in range(len(picturename_list)):
            string = picturename_list[num]
            for files in process_list:
                #print(files,string)
                if search_string(files,string) != string:
                    print('删除',string)
 
 
if __name__=='__main__':
        root_dir=r'E:\gitclone\VUL-project\Rename'#目录
 
        count_files(root_dir)
