# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:54:42 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
max_t = 0
al = None
for x in range(1, 490):
    for y in range(1, 141): 
        for z in range(1, 109): 
            if 2 * x + 7 * y + 9 * z == 979:
                tong = x + y + z
                if tong > max_t:
                    max_t = tong
                    al = (x, y, z)
if al:
    print(f"Bộ nghiệm có tổng lớn nhất là: x = {al[0]}, y = {al[1]}, z = {al[2]}")
    print(f"Tổng x + y + z = {max_t}")
else:
    print("Không tìm thấy bộ nghiệm nào thỏa mãn.")


