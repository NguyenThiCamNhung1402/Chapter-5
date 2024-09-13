# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:51:06 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
n = int(input("Nhập số nguyên dương: "))
while  n <= 0:
    n = int(input("Nhập lại số nguyên dương: "))
x   = False
i = 1
while i * i <= n:
    if i * i == n:
        x   = True
        break
    i += 1
if x :
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
