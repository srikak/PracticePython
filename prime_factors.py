# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:23:00 2024

@author: ksrik
"""

#%% Get input
print("Enter an integer below:")
try:
    n = int(input())
    
except:
    print("Not a proper number!\n")
    
#%% Prime factors

lim = int(n/2) + 1
prime_factors = []
i = 2

while n > 1 and i < lim:
    if n%i == 0:
        prime_factors.append(i)
        n = int(n/i)
        
    else:
        i = i + 1
        
print(f"Prime Factors = {prime_factors}")