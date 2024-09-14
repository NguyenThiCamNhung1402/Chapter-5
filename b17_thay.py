# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:31:50 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))
for i in range(n):
        for j in range(n):
            if j > 0:
                print(" ", end="")  
            print("*", end="")
        print() 
