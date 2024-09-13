# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:15:59 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số nguyên dương n: "))
S = 0
while n <= 0   :
    n = int(input("Không hợp lệ. Nhập lại: "))
for i in range(1, n + 1):
   tong  = i * (i + 1) // 2
   S += (x ** i) /tong 
print("Tổng S là:", S)
