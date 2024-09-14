# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:31:46 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập một số nguyên dương: "))
while n <= 0:
    n = int(input("Nhập lại một số nguyên dương: "))
chuoi_nhi_phan = ""
while n > 0:
    du = n % 2
    chuoi_nhi_phan = str(du) + chuoi_nhi_phan
    n //= 2
if chuoi_nhi_phan == "":
    chuoi_nhi_phan = "0"
print(f"Biểu diễn nhị phân của số nhập vào là: {chuoi_nhi_phan}")

