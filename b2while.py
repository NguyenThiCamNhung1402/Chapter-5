# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:10:13 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
ktra_bien = False  
while not ktra_bien:
    ktr = input("Nhập một số thực trong khoảng [-89.9; 88.8]: ")
    if ktr.replace('.', '', 1).replace('-', '', 1).isdigit() and ktr.count('.') <= 1:
        value = float(ktr)  
        if -89.9 <= value <= 88.8:
            print(f"Giá trị nhập vào hợp lệ: {value}")
            ktra_bien = True 
        else:
            print("Giá trị không nằm trong khoảng [-89.9; 88.8]. Vui lòng nhập lại.")
    else:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số thực.")
