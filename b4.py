# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:15:45 2024

@author: Chi
"""

while True:
    a = int(input("Nhap gia tri tu [-99,99]: "))
    if -99 <= a <= 99:
        print("Hop le", a)
        break
    else:
        print("Khong hop le")