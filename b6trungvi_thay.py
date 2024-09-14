# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:54:16 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
so3 = int(input("Nhập số nguyên thứ ba: "))
so4 = int(input("Nhập số nguyên thứ tư: "))
so5 = int(input("Nhập số nguyên thứ năm: "))
so_list = [so1, so2, so3, so4, so5]
for i in range(5):
    for j in range(0, 5-i-1):
        if so_list[j] > so_list[j+1]:
            so_list[j], so_list[j+1] = so_list[j+1], so_list[j]
trung_vi = so_list[2]
print("Giá trị trung vị là:", trung_vi)

