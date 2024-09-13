# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:26:42 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    thang = input("Nhập số tháng (1-12): ")
    if thang.isdigit():
        thang = int(thang)
        if 1 <= thang <= 12:
            break
    else:
        print("Nhập sai. Thử lại.")
while True:
    nam = input("Nhập số năm: ")
    if nam.isdigit():
        nam = int(nam)
        break
    else:
        print("Nhập sai. Thử lại.")
if thang == 2:
    if (nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
        print("Tháng này có 29 ngày")
    else:
        print("Tháng này có 28 ngày")
else:
    print(f"Tháng này có {ngay[thang - 1]} ngày")

