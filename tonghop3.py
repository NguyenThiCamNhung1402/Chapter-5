# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:14:54 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
id_nguoi_dung = input("Nhập ID user: ")
mat_khau = input("Nhập mật khẩu: ")
id_hop_le = True
if len(id_nguoi_dung) < 6 or len(id_nguoi_dung) > 24:
    id_hop_le = False
else:
    for ky_tu in id_nguoi_dung:
        if ky_tu in "!@#$%^&*()-=+ ":
            id_hop_le = False
            break
mat_khau_hop_le = True
if len(mat_khau) < 6 or len(mat_khau) > 24:
    mat_khau_hop_le = False
else:
    co_chu_thuong = co_so = co_chu_hoa = co_dau_bang = False
    for ky_tu in mat_khau:
        if ky_tu.islower():
            co_chu_thuong = True
        elif ky_tu.isdigit():
            co_so = True
        elif ky_tu.isupper():
            co_chu_hoa = True
        elif ky_tu in "$#@":
            co_dau_bang = True
    if not (co_chu_thuong and co_so and co_chu_hoa and co_dau_bang):
        mat_khau_hop_le = False
if id_hop_le and mat_khau_hop_le:
    print("Đăng nhập thành công.")
else:
    print("Đăng nhập thất bại.")

