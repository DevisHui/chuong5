# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:15:55 2024

@author: Chi
"""

while True:
    a = float(input("Nhap vao so tu [-89.9; 88.8]: "))
    if -89.9 <= a <= 88.8:
        break
    else:
        print("Khong hop le")