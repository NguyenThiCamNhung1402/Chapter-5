# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:07:42 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
n = int(input("Nhập số nguyên dương n: "))
S = 0
while n<= 0 :
    n = int(input("Không hợp lệ. Nhập lại: "))
for i in range(1, n + 1):
    S += 1 / (i * (i + 1))
print("Tổng S là:", S)

