#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import random

temp = {1:'一万',2:'二万',
        3:'三万',4:'四万',
        5:'五万',6:'六万',
        7:'七万',8:'八万',
        9:'九万',10:'十万'
        }
num = [0,0,0,0,0,0,0,0,0,0]
for x in range(1,10000):
    a = random.randint(1,10)
    num [a-1] += 1
print(num)