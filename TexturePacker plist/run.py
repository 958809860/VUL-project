#!/usr/bin/python
import os
def endWith(s,*endstring):          #根据文件扩展名判断文件类型
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def get_process_files(root_dir):    #获取文件路径

    file_list = []
    picture_plist=[]

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            #print('存在的文件：\n',os.path.join(root, name))#文件
            file_list.append(os.path.join(root, name))
        for name in dirs:
            # print('存在的文件夹：\n'os.path.join(root, name))#文件夹
            pass

    for file in file_list:
        if os.path.isfile(file):
            if endWith(file,'.plist') ==True:
                picture_plist.append(file)
        elif os.path.isdir(file):
            dir_extra_list=get_process_files(file)
            if len(dir_extra_list)!=0:
                for x in dir_extra_list:
                    picture_plist.append(x)
    return picture_plist
def run():
    root_dir = "xxx" #这里写资源路径
    for i in get_process_files(root_dir):
        cmd = "python36 "+'.\plistCutter.py'+" " + i.replace("\\","/") + " "+ i.replace("\\","/").replace(".plist",".png")
        print(cmd)
        os.system(cmd)
run()