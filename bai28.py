# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:24:36 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
N = int(input("Nhập số nguyên dương N: "))
while N<= 0:
    N = int(input("Không hợp lệ. Nhập lại: ")) 
print("Các ước số của", N, "là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i) 
     
