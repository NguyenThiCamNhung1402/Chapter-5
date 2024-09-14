# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:31:36 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
i = int(input("Nhập số nguyên i: "))
k = int(input("Nhập cơ số k (2-16): "))
if k < 2 or k > 16:
    print("Cơ số phải nằm trong khoảng từ 2 đến 16")
else:
    ket_qua = ""
    chu_so = "0123456789ABCDEF"  
    while i > 0:
        du = i % k  #
        ket_qua = chu_so[du] + ket_qua  
        i //= k  
    print("Số trong cơ số", k, "là:", ket_qua)


