# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:00:44 2024

@author: ksrik
"""

n = int(input())

flag = 1
i = 2

while flag == 1 and i < int(n*0.5) + 1:
    
    if n%i == 0:
        flag = 0
        print("Not a prime number\n")
        
    else:
        i = i + 1
        
if i == int(n**0.5) + 1:
    print("Prime number\n")