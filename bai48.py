# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:04:04 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
ds = []
min_t = float('inf') 
for z in range(1, 979 // 9 + 1):
    tim = 979 - 9 * z 
    if tim <= 0:
        break
    for y in range(1, tim // 7 + 1):
        if (tim - 7 * y) > 0:  
            x = (tim - 7 * y) / 2 
            if (tim - 7 * y) % 2 == 0 and x > 0:  
                x = int(x) 
                tong = x + y + z 
                if tong < min_t:
                    min_t = tong
                    ds = [(x, y, z)] 
                elif tong == min_t:
                    ds += [(x, y, z)]
print("Các bộ nghiệm nguyên (x, y, z) với x + y + z nhỏ nhất:")
if ds:  
    for i in ds:
        print(i)
else:
    print("Không có bộ nghiệm nào thỏa mãn.")

