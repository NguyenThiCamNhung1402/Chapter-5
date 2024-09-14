# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:03:59 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a, b = i, j
            while b != 0:
                a, b = b, a % b
            if a == 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  
