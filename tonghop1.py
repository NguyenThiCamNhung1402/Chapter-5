# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:18:26 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
chuoi  = input("Nhập chuỗi: ")
print("Độ dài chuỗi:", len(chuoi ))
ki_tu_dac_biet  = "!@#$%^&*()-=+./"
dem_dac_biet   = 0
chu_thuong  = 0
chu_so  = 0
chu_hoa  = 0
for i  in chuoi :
    if i  in ki_tu_dac_biet :
       dem_dac_biet  += 1
    elif i .islower():
       chu_thuong  += 1
    elif i .isdigit():
        chu_so += 1
    elif i .isupper():
        chu_hoa  += 1
print("Số ký tự đặc biệt:", dem_dac_biet )
print("Số ký tự chữ thường [a-z]:", chu_thuong)
print("Số ký tự chữ số [0-9]:", chu_so)
print("Số ký tự chữ hoa [A-Z]:", chu_hoa )
