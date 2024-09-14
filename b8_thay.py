# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:17:30 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import random
n = int(input("Nhập số lượng số ngẫu nhiên: "))
while n <= 0:
    n = int(input ("Số lượng n phải là số nguyên dương:")) 
numbers = [random.random() for i in range(n)]
average = sum(numbers) / n
minimum = min(numbers)
maximum = max(numbers)
print(f"Giá trị trung bình: {average:.4f}")
print(f"Giá trị nhỏ nhất: {minimum:.4f}")
print(f"Giá trị lớn nhất: {maximum:.4f}")

