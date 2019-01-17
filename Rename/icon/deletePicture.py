#!/usr/bin/python
#-*- coding: utf-8 -*-

import os,sys,shutil
movepath = r'E:\gitclone\VUL-project\Rename\icon\新建文件夹'    #将未用到的资源移动到此路径下


def endWith(s,*endstring):          #根据文件扩展名判断文件类型
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def get_process_files(root_dir):    #获取文件路径

    file_list = []
    process_list=[]
    picture_list=[]

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            #print('存在的文件：\n',os.path.join(root, name))#文件
            file_list.append(os.path.join(root, name))
        for name in dirs:
            # print('存在的文件：\n'os.path.join(root, name))#文件夹
            pass

    for file in file_list:
        if os.path.isfile(file):
            if endWith(file,'.ts','.exml') ==True:
                process_list.append(file)
            if endWith(file,'.png','.jpg') ==True:
                picture_list.append(file)
        elif os.path.isdir(file):
            dir_extra_list=get_process_files(file)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    process_list.append(x)
    return process_list,picture_list

def findstring (filename,string):       #在filename的文件中查全称string

    document = open(filename, 'r+', encoding = 'utf-8')
    for each_line in document:
        if each_line.find(string) != -1:   
            return True                 #string存在返回true
    document.close()

def search_string(filename,string):     #在filename的文件中遍历string截掉‘_’后字符串
    if string.find('_') != -1:
        lenstring = len(string.split('_'))
        movefilename = "_".join(string.split('_')[0:(lenstring-1)])  #将最后的_字符串截掉
        #print('movefilename',movefilename)
        if findstring(filename,movefilename) == True:
            return True
        else:
            if search_string(filename,movefilename) == True:
                return True

def count_files(root_dir,root_dir1,root_dir2):
        temp=get_process_files(root_dir)
        temp1=get_process_files(root_dir1)
        temp2=get_process_files(root_dir2)
        process_list=temp[0] + temp1[0] + temp2[0]  #所有json，ts文件的路径
        picture_list=temp2[1]                       #所有png，jpg文件的路径
        #print('\n\nprocess_list=',process_list,'\n\npicture_list=',picture_list)
        for num in range(len(picture_list)):
            string = os.path.basename(picture_list[num]).split('.',1)[0] #获得png或jpg文件名
            account = 0
            for files in process_list:
                #print(files,string)
                if findstring(files,string) == True:                        
                    print('used:',string)

                    break
                else:
                    if search_string(files,string) == True:
                        print('used:',string)
                        break
                    else:
                        if account == len(process_list)-1:
                            shutil.move(picture_list[num],movepath)
                            print('removed:',string,picture_list[num])
                account += 1

if __name__=='__main__':
    root_dir=r'E:\gitclone\VUL-project\Rename\icon\MahjongLobby_XDZPK\Egret\src'#TS文件路径    #sys.argv[1] 使用时加python
    root_dir1=r'E:\gitclone\VUL-project\Rename\icon\MahjongLobby_XDZPK\Egret\resource\lobbySkins'#EXML文件路径
    root_dir2=r'E:\gitclone\VUL-project\Rename\icon\MahjongLobby_XDZPK\resource'#图片路径
    count_files(root_dir,root_dir1,root_dir2)