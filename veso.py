# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:38:06 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import random
so_ve = int(input("Nhập số lượng vé bạn muốn mua: "))
gia_ve = 10000
tong_tien_tra = so_ve * gia_ve
danh_sach_ve = [[0] * 6 for _ in range(so_ve)]  
for i in range(so_ve):
    ve = danh_sach_ve[i]
    so_count = 0
    while so_count < 6:
        so = random.randint(1, 45)
        if so not in ve:
            ve[so_count] = so
            so_count += 1
    print(f"Vé {i+1}: {ve}")
so_trung = [0] * 6
so_count = 0
while so_count < 6:
    so = random.randint(1, 45)
    if so not in so_trung:
        so_trung[so_count] = so
        so_count += 1
print(f"Dãy số trúng thưởng: {so_trung}")
tong_tien_thang = 0
for i in range(so_ve):
    ve = danh_sach_ve[i]
    trung_nhau = 0
    for so in ve:
        for so_trung_item in so_trung:
            if so == so_trung_item:
                trung_nhau += 1
    if trung_nhau == 6:
        tien_thang = 10000000000
    elif trung_nhau == 5:
        tien_thang = 10000000
    elif trung_nhau == 4:
        tien_thang = 300000
    elif trung_nhau == 3:
        tien_thang = 30000
    else:
        tien_thang = 0
    print(f"Vé {i+1}: Trúng {tien_thang} VND")
    tong_tien_thang += tien_thang
print(f"Tổng tiền bạn đã trả: {tong_tien_tra} VND")
print(f"Tổng tiền bạn đã trúng: {tong_tien_thang} VND")
