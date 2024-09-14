# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:42:36 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
ds_n = [2, 4, 8, 16, 32, 64, 128]
print(f"{"n":<10}{"log(n)":<15}{"n log(n)":<15}{"n^2":<15}{"n^3":<15}")
for n in ds_n:
    if n == 2:
        log_n = 0.3010
    elif n == 4:
        log_n = 0.6021
    elif n == 8:
        log_n = 0.9031
    elif n == 16:
        log_n = 1.2041
    elif n == 32:
        log_n = 1.5051
    elif n == 64:
        log_n = 1.8062
    elif n == 128:
        log_n = 2.1072
    else:
        log_n = 0  
    n_log_n = n * log_n
    n_binh_2 = n ** 2
    n_binh_3 = n ** 3
    print(f"{n:<10}{log_n:<15.4f}{n_log_n:<15.4f}{n_binh_2:<15}{n_binh_3:<15}")
