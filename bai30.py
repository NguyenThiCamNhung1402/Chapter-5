# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:26:42 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
month = int(input("Nhập tháng (1-12): "))
while month < 1 or month > 12:
    month = int(input("Tháng không hợp lệ. Vui lòng nhập lại: "))
year = int(input("Nhập năm: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days= 29
  else:
     days = 28
print(f"Tháng {month} năm {year} có {days} ngày.")
