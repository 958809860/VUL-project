#!/usr/bin/env python
#-*- coding: utf-8 -*-
import win32api
import os
from PIL import ImageGrab,Image
import pyHook
import pythoncom
 
# 创建一个坐标列表(x1,y1,x2,y2)
coordinate = [1, 1, 1, 1]
 
# 监听键盘事件
def on_mouse_event(event):
    file_path = r'C:\Users\VULCAN\Desktop\image.png'
    # 监听鼠标事件
    if event.MessageName == 'mouse left down':
        coordinate[0:2] = event.Position    
    elif event.MessageName == 'mouse left up':
        coordinate[2:4] = event.Position
        win32api.PostQuitMessage()  # 退出监听循环
        # 截取坐标图片
        pic = ImageGrab.grab(coordinate)
        pic.save(file_path)
