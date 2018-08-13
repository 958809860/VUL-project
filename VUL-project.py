#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

cwd = os.getcwd()
print(cwd)

def cmd(args):
    pass

print(cmd)

dstDir= "./VUL-project"
if os.path.exists(dstDir) == False:#如果没有，则clone下
	# os.system("mkdir -p %s"%(dstDir))
    cmd = cmd = ("git clone clone https://github.com/958809860/VUL-project.git %s"%(dstDir))
os.chdir(dstDir)
os.system("pwd")
try:
    cmd = "git pull"
    print(cmd)
    os.system(cmd)
    print("VUL-project-git pull 完成!!")
except BaseException as e:
    print("git pull error！")
    wait = input()

cmd = "start table"
os.system(cmd)
