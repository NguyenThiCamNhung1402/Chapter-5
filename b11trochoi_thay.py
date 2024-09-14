# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:10 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import random
n = int(input("Nhập số lần chơi: "))
thang_khong_chuyen = 0
thang_chuyen = 0
for _ in range(n):
    cua_giai_thuong = random.randint(0, 2)
    cua_chon = random.randint(0, 2)
    for cua in [0, 1, 2]:
        if cua != cua_giai_thuong and cua != cua_chon:
            cua_mo = cua
            break
    if cua_chon == cua_giai_thuong:
        thang_khong_chuyen += 1
    for cua in [0, 1, 2]:
        if cua != cua_chon and cua != cua_mo:
            cua_chuyen = cua
            break
    if cua_chuyen == cua_giai_thuong:
        thang_chuyen += 1
ty_le_khong_chuyen = thang_khong_chuyen / n
ty_le_chuyen = thang_chuyen / n
print("Tỷ lệ thắng khi không đổi cửa:", ty_le_khong_chuyen)
print("Tỷ lệ thắng khi đổi cửa:", ty_le_chuyen)

