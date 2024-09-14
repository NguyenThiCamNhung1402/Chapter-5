# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:13:04 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))
for a in range(1, n + 1):
    a3 = a ** 3
    for b in range(a + 1, n + 1):  
        b3 = b ** 3
        tong1 = a3 + b3
        for c in range(1, n + 1):
            c3 = c ** 3
            for d in range(c + 1, n + 1):  
                d3 = d ** 3
                tong2 = c3 + d3
                if tong1 == tong2 and a != c and a != d and b != c and b != d:
                    print(f"{a}^3 + {b}^3 = {c}^3 + {d}^3")


