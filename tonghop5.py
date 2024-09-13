# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:57:35 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""

import random
ds  = ["Kéo", "Búa","Bao"]
so_nguoi  = random.randint(8, 20)
print(f"Số lượng người chơi: {so_nguoi }")
nguoi_chon  = [random.choice(ds ) for _ in range(so_nguoi )]
i = 1
for x  in nguoi_chon :
    print(f"Người chơi {i} chọn: {x }")
    i += 1
dem_keo  = nguoi_chon .count("Kéo")
dem_bua  = nguoi_chon .count("Búa")
dem_bao  = nguoi_chon .count("Bao")
print(f"Số người chọn Kéo: {dem_keo }")
print(f"Số người chọn Búa: {dem_bua }")
print(f"Số người chọn Bao: {dem_bao }")
if dem_keo  > dem_bua  and dem_keo  > dem_bao :
    print("Kéo thắng!")
elif dem_bua  > dem_keo  and dem_bua  > dem_bao :
    print("Búa thắng!")
elif dem_bao  > dem_keo  and dem_bao  > dem_bua :
    print("Bao thắng!")
else:
    print("Hòa!")
