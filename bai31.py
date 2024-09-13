# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:39:52 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
if a <= 0 or b <= 0 or c <= 0:
    loai = "Các cạnh phải là số nguyên dương"
else:
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a + b > c:
        if a == b == c:
            loai = "Tam giác đều"
        elif a**2 + b**2 == c**2:
            loai = "Tam giác vuông"
        elif a == b or b == c or a == c:
            loai = "Tam giác cân"
        else:
            loai = "Tam giác thường"
    else:
        loai = "Ba số không lập thành tam giác"
print("Kết quả kiểm tra:", loai)


