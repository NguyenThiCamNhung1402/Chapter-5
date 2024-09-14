# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:54:16 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
p_khong_1 = 5 / 6
p_it_nhat_1_6 = 1 - p_khong_1 ** 6
n = 12
p_1 = 1 / 6
p_khong_1_12 = (1 - p_1) ** n
p_1_12 = n * p_1 * (1 - p_1) ** (n - 1)
p_it_nhat_2_12 = 1 - (p_khong_1_12 + p_1_12)
print("Xác suất ít nhất một số 1 trong 6 lần gieo:", p_it_nhat_1_6)
print("Xác suất ít nhất hai số 1 trong 12 lần gieo:", p_it_nhat_2_12)
if p_it_nhat_1_6 > p_it_nhat_2_12:
    print("Nhận ít nhất một số 1 khi gieo xúc xắc sáu lần có khả năng xảy ra hơn.")
else:
    print("Nhận ít nhất hai số 1 khi gieo xúc xắc 12 lần có khả năng xảy ra hơn.")

