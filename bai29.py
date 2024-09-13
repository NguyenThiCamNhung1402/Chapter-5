# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:24:51 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471  
"""
N = int(input("Nhập số nguyên dương N: "))
while N <= 0:
    N = int(input("Không hợp lệ. Nhập lại số nguyên dương: "))
tong = 0
so_du = N
while so_du > 0:
    tong += so_du % 10  
    so_du //= 10       
print("Tổng các chữ số của", N, "là:", tong)
