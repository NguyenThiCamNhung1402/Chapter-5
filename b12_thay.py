# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:15:42 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
so_luong = 100
a, b = 0, 1
print("100 số đầu tiên của dãy Fibonacci là:")
for i in range(so_luong):
    print(a, end=" ")
    a, b = b, a + b

