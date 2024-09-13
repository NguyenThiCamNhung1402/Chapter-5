# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:54:42 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
tong_lon_nhat = 0
bo_nghiem_tot_nhat = [(0, 0, 0)] * 100  
so_luong_nhiem = 0  
for x in range(1, 980 // 2 + 1):
    for y in range(1, 980 // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z.is_integer() and z > 0:
            z = int(z)
            tong_hien_tai = x + y + z
            if tong_hien_tai > tong_lon_nhat:
                tong_lon_nhat = tong_hien_tai
                so_luong_nhiem = 1
                bo_nghiem_tot_nhat[0] = (x, y, z)
            elif tong_hien_tai == tong_lon_nhat:
                bo_nghiem_tot_nhat[so_luong_nhiem] = (x, y, z)
                so_luong_nhiem += 1
print("Tất cả bộ nghiệm (x, y, z) với tổng x + y + z lớn nhất:")
for i in range(so_luong_nhiem):
    print(bo_nghiem_tot_nhat[i])


