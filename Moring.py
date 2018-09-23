#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xlwt
def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False
 
# 定义要创建的目录
cwd = os.path.dirname(os.getcwd())
os.chdir(cwd)
mkpath="moring"
# 调用函数
mkdir(mkpath)

Excel = r"./moring/moring记录.xlsx"
TXT = r"./moring/moring.txt"

book = xlwt.Workbook(encoding='utf-8', style_compression=0) #创建一个xls
sheet = book.add_sheet('dede', cell_overwrite_ok=True) #在xls中创建一个sheet
col_2  = sheet.col(1) #选中第二列
col_2.width = 256*20 #修改第二列宽度
col_3 = sheet.col(2) #选中第三列
col_3.width = 256*50 #修改第三列宽度
col_6 = sheet.col(7) #选中第七列
col_6.width = 256*37 #修改第七列宽度
row0 = ['编号', '项目', '工件', '负责人', '预计时间', '剩余时间','日期']
postType = ['前端', '策划', '美术', '后端', '测试']
postType2 = ['编','#']
postType3 = ['#编','# ']
for i in range(0, len(row0)):#写入标题行
    sheet.write(0, i, row0[i])
try:
    document = open(TXT, 'r+')
except BaseException:
    print("请将moring.txt放在：moring文件夹中，再尝试")
    wait = input()
line = 1
time = 0
pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style = xlwt.XFStyle() # Create the Pattern
style.pattern = pattern # Add Pattern to Style

def writeExcel (line ,item): #写入Excel
    item.append("")
    for y in range(0, 8):
        if len(item[2])<3:
            print("********************[error]********************")
            print(item)
            print("错误原因：已写入请查看是否格式正确！！")
            print("***********************************************")
            item[7] = "错误原因：已写入请查看是否格式正确！！"
            sheet.write(line, y, item[y],style)
        else:
            sheet.write(line, y, item[y])

def nameJudge (each_line,time):  #截取name,time
    time = each_line.split(' ')[2]
    each_line = each_line.split(' ', 1)[1].split('(', 1)[0].split('<', 1)[0]
    if len(each_line) > 7:
        each_line = each_line.split('1', 1)[0]
    if each_line[:1] == ' ':
        each_line = each_line.split(' ')[1]
    return each_line,time

for each_line in document:
    if each_line == '\n': #空行跳过
        each_line = each_line.split('\n')
    if each_line[:2] in postType:
        try:
            name,time= nameJudge(each_line,time)
        except BaseException:
            print("**************无用信息执行——跳过***************")
    else:
         try:
            hang = each_line #方便后续工作
            each_line = each_line.replace('# ', '#编号 ', 1)
            each_line = each_line.replace('#', '', 1).replace('+', '+ ', 1).replace('-', '- ', 1).replace(' -', '- ', 1) #格式修正
            item1 = each_line.split()[0]
            item2 = each_line.split()[1]
            item3 = each_line.split()[2]
            item4 = name
            item5 = each_line.split()[3].split('-', 1)[0]
            try:
                item6 = each_line.split()[4]
            except IndexError:
                if hang[0] in postType2 and hang[1] not in postType3:
                    hang = hang.replace('#', '#编号 ', 1)
                    hang = hang.replace('#', '', 1).replace('+', '+ ', 1).replace('-', '- ', 1).replace(' -', '- ',1)  # 格式修正
                    item1 = '编号'
                    item2 = each_line.split()[0]
                    item3 = each_line.split()[1]
                    item5 = each_line.split()[2].split('-', 1)[0]
                    item6 = each_line.split()[3]
                else:
                    item6 = item5
            item7 = time
            item = [item1,item2,item3,item4,item5,item6,item7]
            if item[4].isdigit() == True: #判断预估时间是否是数字
                writeExcel(line , item)
                line = line + 1
                print(item)#编译检查
            else:
                abc = each_line.split()[2]+each_line.split()[3]
                itemx = [each_line.split()[0], each_line.split()[1], abc, name, each_line.split()[4].split('-', 1)[0], each_line.split()[5],time]
                writeExcel(line , itemx)
                line = line + 1
                print(itemx)#编译检查
         except BaseException:
            if hang[0] in postType2:
                print("********************[error]********************")
                print("错误行数：（不计算name行）", line, "错误人员：", name, "\n", hang.split('\n')[0])
                print("错误原因：历史工件书写错误")
                print("***********************************************")
                #break   #错误停止（如果屏蔽，跳过错误行）
            else:
                print("**************无用信息执行——跳过***************")
try:
    book.save(Excel)
    print('保存成功')
    print (os.getcwd())
    cmd = "start moring/moring记录.xlsx"
    print(cmd)
    os.system(cmd)
except PermissionError:
    cmd = 'taskkill /f /im "et.exe"'
    print(cmd)
    os.system(cmd)
    book.save(Excel)
    print('保存成功')
    cmd = "start moring/moring记录.xlsx"
    print(cmd)
    os.system(cmd)
wait = input()