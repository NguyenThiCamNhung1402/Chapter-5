# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:09:28 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
so_lan_in = int(input("Nhập số lần in dòng chữ 'Hello' (nhỏ hơn 1000): "))
while  so_lan_in<= 0 or so_lan_in > 1000:
    so_lan_in= int(input( "Số lần in phải nằm trong khoảng từ 0 đến 999:"))
for i in range(so_lan_in):
    print("Hello")


