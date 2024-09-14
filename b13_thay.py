# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:15:47 2024

@author:  Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int( input("Nhập giá trị n: ")) 
while n <= 0:
    n =int(input("Nhập lại giá trị n: ")) 
luy_thua_2 = 1
while luy_thua_2 <= n:
    print(luy_thua_2)
    luy_thua_2 *= 2

