# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:39:52 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
while a <= 0 or b <= 0 or c <= 0:
    a = int(input("Nhập lại cạnh thứ nhất: "))
    b = int(input("Nhập lại cạnh thứ hai: "))
    c = int(input("Nhập lại cạnh thứ ba: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        loai = "Tam giác đều"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        loai = "Tam giác vuông"
    elif a == b or b == c or a == c:
        loai = "Tam giác cân"
    else:
        loai = "Tam giác thường"
else:
    loai = "Ba số không lập thành tam giác"

print("Kết quả kiểm tra:", loai)
