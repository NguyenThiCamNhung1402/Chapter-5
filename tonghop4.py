# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:23:45 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""

import random

ds  = ["Kéo", "Búa", "Bao"]
nguoi_chon  = ""
while nguoi_chon  != "thoát":
    nguoi_chon  = input("Chọn Kéo, Búa, hoặc Bao (hoặc nhập 'thoát' để dừng): ")
    if nguoi_chon  == "thoát":
        print("Trò chơi kết thúc.")
        break
    if nguoi_chon  not in ds :
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        continue
    may_chon  = random.choice(ds )
    print(f"Máy chọn: {may_chon }")
    if nguoi_chon  == may_chon :
        print("Hòa!")
    elif (nguoi_chon  == 'Kéo' and may_chon  == 'Bao') or \
         (nguoi_chon  == 'Búa' and may_chon  == 'Kéo') or \
         (nguoi_chon  == 'Bao' and may_chon  == 'Búa'):
        print("Bạn thắng!")
    else:
        print("Máy thắng!")
