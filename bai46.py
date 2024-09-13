# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:33:46 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
nghiem  = []
for x in range(1, 980):
    for y in range(1, 980):
        if (979 - 2 * x - 7 * y) % 9 == 0:
            z = (979 - 2 * x - 7 * y) // 9
            if z > 0:
                nghiem += [(x, y, z)]
print("Các bộ nghiệm nguyên của phương trình 2x + 7y + 9z = 979 là:")
for i  in nghiem :
    print(i )
