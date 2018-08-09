#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

cwd = os.getcwd()
print(cwd)

def cmd(args):
    pass

print(cmd)

dstDir= "./MahjongLobbyCommon"
if os.path.exists(dstDir) == False:#如果没有，则clone下
	# os.system("mkdir -p %s"%(dstDir))
    cmd = cmd = ("git clone clone git@git.code4.in:Mahjong.jx/MahjongLobbyCommon.git %s"%(dstDir))
os.chdir(dstDir)
os.system("pwd")
try:
    cmd = "git pull"
    print(cmd)
    os.system(cmd)
    print("MahjongLobbyCommon-git pull 完成!!")
except BaseException as e:
    print("git pull error！")
    wait = input()

cmd = "start table"
os.system(cmd)
