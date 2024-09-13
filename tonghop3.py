# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:14:54 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471 
"""
user_id = input("Nhập ID user: ")
password = input("Nhập mật khẩu: ")
user_valid = True
if len(user_id) < 6 or len(user_id) > 24:
    user_valid = False
else:
    for c in user_id:
        if c in "!@#$%^&*()-=+ ":
            user_valid = False
            break
password_valid = True
if len(password) < 6 or len(password) > 24:
    password_valid = False
else:
    has_lower = has_digit = has_upper = has_special = False
    for c in password:
        if c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c.isupper():
            has_upper = True
        elif c in "$#@":
            has_special = True
    if not (has_lower and has_digit and has_upper and has_special):
        password_valid = False
if user_valid and password_valid:
    print("Đăng nhập thành công.")
else:
    print("Đăng nhập thất bại.")
