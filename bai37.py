# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:47:47 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
n = int(input("Nhập số chẵn n lớn hơn 0: "))
S = 0
while n <= 0 or n % 2 != 0:
    n = int(input("Không hợp lệ. Nhập lại số chẵn n lớn hơn 0: "))
for i in range(2, n + 1, 2):
    S += i
print("Tổng S là:", S)

