# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:24:51 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471  
"""
N = int(input("Nhập số nguyên dương N: "))
while N <= 0:
    N = int(input("Không hợp lệ. Nhập lại số nguyên dương: "))
tong = 0
while n  > 0:
    tong += n  % 10  
    n  //= 10       
print("Tổng các chữ số là:", tong)
