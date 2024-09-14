# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:44:34 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
ma_nhan_vien: str
ho_ten: str
luong_co_ban: float  
luong_hang_thang: float  
so_ngay: int 
so_san_pham: int
nv_van_phong = [
    {
        "ma_nhan_vien": "VP001",
        "ho_ten": "Nguyễn Văn A",
        "luong_co_ban": 5000000,
        "luong_hang_thang": 6000000,
        "so_ngay": 22
    },
    {
        "ma_nhan_vien": "VP002",
        "ho_ten": "Trần Thị B",
        "luong_co_ban": 6000000,
        "luong_hang_thang": 7000000,
        "so_ngay": 21
    },
    {
        "ma_nhan_vien": "VP003",
        "ho_ten": "Lê Văn C",
        "luong_co_ban": 5500000,
        "luong_hang_thang": 7200000,
        "so_ngay": 23
    },
    {
        "ma_nhan_vien": "VP004",
        "ho_ten": "Phạm Văn D",
        "luong_co_ban": 5200000,
        "luong_hang_thang": 7100000,
        "so_ngay": 20
    },
    {
        "ma_nhan_vien": "VP005",
        "ho_ten": "Nguyễn Thị E",
        "luong_co_ban": 5800000,
        "luong_hang_thang": 7300000,
        "so_ngay": 22
    }
]
nv_ban_hang = [
    {
        "ma_nhan_vien": "BH001",
        "ho_ten": "Lê Thị F",
        "luong_co_ban": 4000000,
        "luong_hang_thang": 6000000,
        "so_san_pham": 120
    },
    {
        "ma_nhan_vien": "BH002",
        "ho_ten": "Phạm Văn G",
        "luong_co_ban": 4500000,
        "luong_hang_thang": 6200000,
        "so_san_pham": 130
    },
    {
        "ma_nhan_vien": "BH003",
        "ho_ten": "Nguyễn Thị H",
        "luong_co_ban": 4200000,
        "luong_hang_thang": 6100000,
        "so_san_pham": 140
    },
    {
        "ma_nhan_vien": "BH004",
        "ho_ten": "Trần Văn I",
        "luong_co_ban": 4300000,
        "luong_hang_thang": 6300000,
        "so_san_pham": 110
    },
    {
        "ma_nhan_vien": "BH005",
        "ho_ten": "Lê Văn K",
        "luong_co_ban": 4400000,
        "luong_hang_thang": 6200000,
        "so_san_pham": 150
    }
]
print("Thông tin nhân viên văn phòng:")
for nv in nv_van_phong:
    print(f"Mã nhân viên: {nv['ma_nhan_vien']}")
    print(f"Họ và tên: {nv['ho_ten']}")
    print(f"Lương cơ bản: {nv['luong_co_ban']} VND")
    print(f"Lương hàng tháng: {nv['luong_hang_thang']} VND")
    print(f"Số ngày làm việc: {nv['so_ngay']}\n")
print("Thông tin nhân viên bán hàng:")
for nv in nv_ban_hang:
    print(f"Mã nhân viên: {nv['ma_nhan_vien']}")
    print(f"Họ và tên: {nv['ho_ten']}")
    print(f"Lương cơ bản: {nv['luong_co_ban']} VND")
    print(f"Lương hàng tháng: {nv['luong_hang_thang']} VND")
    print(f"Số sản phẩm: {nv['so_san_pham']}\n")

