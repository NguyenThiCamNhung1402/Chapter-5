# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:04:09 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
# a. Kết quả: j= 45 
j = 0
for i in range(0, 10):
        j += i
print(j )
# b. Kết quả: j= 1024 
j = 1
for i in range(0, 10):
        j += j
print(j )
# c. Kết quả: j= 18 
for j in range(0, 10):
        j += j
print(j )
