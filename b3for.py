# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:03:50 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""

import random
ngau_nhien = random.randint(20, 30)
ds = [i for i in range(ngau_nhien)]
print("Danh sách:", ds)
print("Số lượng phần tử:", len(ds))
so_luong_so = 10
ds_binh_phuong = [0] * so_luong_so
for x in range(so_luong_so):
    so_thuc = random.uniform(18, 99)  
    binh_phuong = so_thuc ** 2  
    ds_binh_phuong[x] = binh_phuong  
print("Danh sách các giá trị bình phương:", ds_binh_phuong)
