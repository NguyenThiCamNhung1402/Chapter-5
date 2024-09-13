# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:49:44 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
n = int(input("Nhập số lẻ n lớn hơn 0: "))
S=1 
while  n <= 0 or  n % 2== 0:
    n = int(input("Không hợp lệ. Nhập lại:"))
for i in range(1, n + 1):
    S *= i
print("Tích S là:", S)



