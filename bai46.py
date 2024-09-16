# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:33:46 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
for x in range(1, 980//2):  
    for y in range(1, (980 - 2*x)//7 + 1):  
        for z in range(1, (980 - 2*x - 7*y)//9 + 1):  
            if 2*x + 7*y + 9*z == 979:
                print(f"Bộ nghiệm: x = {x}, y = {y}, z = {z}")

