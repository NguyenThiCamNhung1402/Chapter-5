# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:16:14 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
email = input("Nhập địa chỉ email để kiểm tra: ")
ten_mien_hop_le = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]
vi_tri_a_cong = -1
vi_tri_cham = -1
for i in range(len(email)):
    if email[i] == "@":
        vi_tri_a_cong = i
    elif email[i] == ".":
        vi_tri_cham = i
if vi_tri_a_cong != -1 and  vi_tri_cham != -1 and  vi_tri_cham > vi_tri_a_cong:
    phan_ten_nguoi_dung = email[:vi_tri_a_cong]
    phan_ten_mien = email[vi_tri_a_cong + 1:]
    ten_mien_hop_le_khong = False
    for ten_mien in ten_mien_hop_le:
        if phan_ten_mien == ten_mien:
            ten_mien_hop_le_khong = True
            break
    ten_nguoi_dung_hop_le = len(phan_ten_nguoi_dung) >= 6
    for ky_tu in phan_ten_nguoi_dung:
        if ky_tu in " \t\r\n!#$%&\"*+/=?^_`{|}~":
            ten_nguoi_dung_hop_le = False
            break
    if ten_mien_hop_le_khong and ten_nguoi_dung_hop_le:
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.")
else:
    print("Địa chỉ email không hợp lệ.")

