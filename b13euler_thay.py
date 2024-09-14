# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:18 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
gioi_han = 150  
for a in range(1, gioi_han):
    a_mu_5 = a ** 5
    for b in range(a, gioi_han):
        b_mu_5 = b ** 5
        for c in range(b, gioi_han):
            c_mu_5 = c ** 5
            for d in range(c, gioi_han):
                d_mu_5 = d ** 5
                tong_mu_5 = a_mu_5 + b_mu_5 + c_mu_5 + d_mu_5
                for e in range(d + 1, gioi_han):
                    e_mu_5 = e ** 5
                    if e_mu_5 == tong_mu_5:
                        print(f"{a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")

