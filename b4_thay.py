# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:13:15 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập số nguyên n: "))
if n > 2:
    so_nguyen_to = [True] * n
    so_nguyen_to[0] = so_nguyen_to[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if so_nguyen_to[i]:
            for j in range(i * i, n, i):
                so_nguyen_to[j] = False
    dem = 0
    for i in range(n):
        if so_nguyen_to[i]:
            dem += 1
    print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem)
else:
    print("Số nguyên n phải lớn hơn 2.")

