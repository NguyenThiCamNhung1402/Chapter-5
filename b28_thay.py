# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:03:56 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))
a = x
b = y
while b != 0:
    a, b = b, a % b
print("Ước chung lớn nhất (GCD) của", x, "và", y, "là:", a)

