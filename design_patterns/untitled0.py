#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:26:23 2021

@author: vijay
"""
arr = [0, 2, 1, 0, 1, 2, 0]

ln = len(arr)
for i in range(ln):
    if arr[i]==0:
        i1=arr.pop(i)
        arr.insert(0, i1)
    elif arr[i]==2:
        i1=arr.pop(i)
        arr.insert(-1, i1)
    else:
        i1=arr.pop(i)
        arr.insert(arr.index(2), i1)
ar
A,B,C,D,E,F,G
X,Y,Z-F

s="Type copyright, credits or license"
import re
s1=re.sub(r'\W+', '-', s)
s1

import requests
url = "https://123mkv.surf/start-downloading/"
data = {'fname':'Radhe.2021.x264.720p.WebHD.Hindi.AAC.mkv',
        'fsip':'srv3.securedown.xyz'}
print(requests.post(url, data).text)
"ssss aaa".title()

test_dict = {"Gfg" : {1}, "Best" : None, "is" : {}}
any(test_dict.values())

import math

value = 0.1
step_size = math.ceil(value/6)
print(step_size)
total = step_size
while total < value:
    total += step_size
total += step_size
print(total)

#Ajax-- Ranking and diversity, Placement
exam_list=((2, 'JEE Main Paper 1'),)
counselling_list=((550, 'Central Seat Allocation Board'), (548, 'Joint Seat Allocation Authority'))
print(exam_list[0][0], counselling_list[0][0])
href='https://www.google.com/amp/s/engineering.careers360.com/articles/jee-main-cutoff/amp'
href.lower().find('careers360.mob')

ids=[2,4,3,1,5]
sorted(ids[:1])

s="a b c d e f g h/"
s[:-1]

p=round(89.5)
m=p%20
if m>=10:
    tp = p-m+20
else:
    tp=p-m
tp={'gn':"gn",'t':0}
all(tp.values())
t=(1,2)
t=t+(3,)
t
