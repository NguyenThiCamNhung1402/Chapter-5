# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:16:02 2024

@author:  Nguyễn Thị Cẩm Nhung - 23712471
"""
# Tính tổng nghịch đảo bình phương:
total =0 
n= int(input("Nhập: "))
for i in range(1, n+1):
    total += 1.0 / (i*i)
print(total )
# Hoặc:
for i in range(1, n+1):
        total += 1 / (1.0*i*i) 
print(total )

   

    

