# -*- coding: utf-8 -*-
import os
import re

stringlist = ['通辽','Cmd.ShowActionRoomCmd_CS','1103127']
TXT = r'./tdkserver.log.181219-15'

document = open(TXT, 'r+', encoding = 'utf-8')
count = 0
def searchstring(each_line):
        for i in range(len(stringlist)):
                if each_line.find(stringlist[i]) != -1:
                        pass
                else:
                        return False
if __name__=='__main__':
        for each_line in document:
                count += 1 
                if searchstring(each_line) != False:
                        print(count , each_line)
