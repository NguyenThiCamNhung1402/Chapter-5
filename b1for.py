# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:59:44 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""

n = int(input("Nhập số nguyên dương n: "))
giai_thua = 1
while n<=0:
    n = int(input("Nhập lại số nguyên dương n: "))
for i in range(1, n + 1):
    giai_thua *= i
print(f"Giai thừa của {n} là {giai_thua}")