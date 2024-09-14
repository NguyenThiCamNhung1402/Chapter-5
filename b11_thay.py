# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:13:38 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
# Kết quả: m= 987654321 n=0 
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
print(m, n )