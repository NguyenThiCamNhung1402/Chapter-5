# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:13:12 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
so_9_chu_so = input("Nhap so nguyen 9 chu so: ")
if len(so_9_chu_so) == 9 and so_9_chu_so.isdigit():
    chu_so = [int(x) for x in so_9_chu_so]
    tong = 0
    for i in range(9):
        tong += (10 - i) * chu_so[i]
    chu_so_kiem_tra = 0
    for d1 in range(10):
        if (tong + d1) % 11 == 0:
            chu_so_kiem_tra = d1
            break
    for i in range(9):
        print(chu_so[i], end="")
    if chu_so_kiem_tra == 10:
        print("X", end="")
    else:
        print(chu_so_kiem_tra, end="")
    print()
else:
    print("So nhap vao khong hop le.")


