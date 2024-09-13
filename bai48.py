# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:04:04 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
tong_nho_nhat = float('inf')   
bo_nghiem_toi_uu = [(0, 0, 0)] * 100  
so_luong_nhiem = 0  
for x in range(1, 980 // 2 + 1):
    for y in range(1, 980 // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z.is_integer() and z > 0:
            z = int(z)
            tong_hien_tai = x + y + z
            if tong_hien_tai < tong_nho_nhat:
                tong_nho_nhat = tong_hien_tai
                so_luong_nhiem = 1  
                bo_nghiem_toi_uu[0] = (x, y, z)  
            elif tong_hien_tai == tong_nho_nhat:
                bo_nghiem_toi_uu[so_luong_nhiem] = (x, y, z)  
                so_luong_nhiem += 1  
print("Tất cả bộ nghiệm (x, y, z) với tổng x + y + z nhỏ nhất:")
for i in range(so_luong_nhiem):
    print(bo_nghiem_toi_uu[i])

