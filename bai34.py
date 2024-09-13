# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:20:47 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
n = int(input("Nhập số nguyên dương: "))
while  n<= 0:
    n = int(input("Nhập lại số nguyên dương: "))
if n == 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
