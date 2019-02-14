#!/usr/bing/env python
# -*- coding: utf-8 -*-
import os,sys
sys.path.append(r'./')
import imagesimilarity

def endWith(s,*endstring):          #根据文件扩展名判断文件类型
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def get_process_files(root_dir):    #获取文件路径

    file_list = []
    png_list=[]
    jpg_list=[]

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            #print('存在的文件：\n',os.path.join(root, name))#文件
            file_list.append(os.path.join(root, name))
        for name in dirs:
            # print('存在的文件夹：\n'os.path.join(root, name))#文件夹
            pass

    for file in file_list:
        if os.path.isfile(file):
            if endWith(file,'.png') ==True:
                png_list.append(file)
            if endWith(file,'.jpg') ==True:
                jpg_list.append(file)

    print(len(png_list),len(jpg_list))
    return png_list,jpg_list
compare_image = imagesimilarity.CompareImage()
def compareimage(imagelist):
    samecount = 0
    similarcount = 0
    count = 0
    for image in imagelist:
        count += 1
        image2 = imagelist[count:]
        for imagenext in image2:
            result = compare_image.compare_image(image,imagenext)
            fileresult.write('Compare the image result is: ' + str(result) + '\n') 
            if  result == 1 :
                samecount +=1
                print(image,imagenext)
                fileresult.write('sameimage:' + str(image) + str(imagenext) + '\n')
            if result >= 0.9 and result < 1:
                similarcount +=1
                print('Compare the image result is similar: ' + str(result))
    return samecount,similarcount
png_list,jpg_list = get_process_files(r'E:\gitclone\VUL-project\Rename\icon\DeZhouPuKe - master\resource\atlas\card_style1')

fileresult = open('result.txt','a', encoding = 'utf-8')
samecount,similarcount = compareimage(png_list)
fileresult.write('png_list:' +str(len(png_list)) +'----samecount:'+str(samecount)+'  similarcount:'+str(similarcount))
samecount,similarcount = compareimage(jpg_list)
fileresult.write('\njpg_list:'+str(len(jpg_list)) +'----samecount:'+str(samecount)+'  similarcount:'+str(similarcount))
fileresult.close()