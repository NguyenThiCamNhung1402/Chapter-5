# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:16:14 2024

@author: Nguyễn Thị Cẩm Nhung -23712471 
"""
email = input("Nhập địa chỉ email để kiểm tra: ")
valid_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com']
at_index = -1
dot_index = -1
for i in range(len(email)):
    if email[i] == '@':
        at_index = i
    elif email[i] == '.':
        dot_index = i
if at_index != -1 and dot_index != -1 and dot_index > at_index:
    user_part = email[:at_index]
    domain_part = email[at_index + 1:]
    domain_valid = False
    for domain in valid_domains:
        if domain_part == domain:
            domain_valid = True
            break
    user_valid = len(user_part) >= 6
    for c in user_part:
        if c in ' \t\r\n!#$%&\'*+/=?^_`{|}~':
            user_valid = False
            break
    if domain_valid and user_valid:
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.")
else:
    print("Địa chỉ email không hợp lệ.")
