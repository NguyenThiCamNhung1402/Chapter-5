# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:24:36 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
while True:
    N = input("Nhập số nguyên dương N: ")
    if N.isdigit():
        N = int(N)
        if N > 0:
            break
    else:
        print("Số nhập vào không hợp lệ! Vui lòng nhập lại.")
print("Các ước số của", N, "là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
     