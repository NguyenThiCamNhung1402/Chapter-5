# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:13:57 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
count = 0
for num in range(1000, 2000):
    print(num, end=' ')
    count += 1
    if count % 5 == 0:
        print()

