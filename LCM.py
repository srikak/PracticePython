# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:46:54 2024

@author: ksrik
"""

import numpy as np

#%% Get input
print("Enter an integers below:")
try:
    n = list(map(int, input().split(",")))
except:
    print("Not a proper number!\n")
    
#%% Functions - Factorise

def factorise(n):
    lim = np.ceil(n/2) + 1
    prime_factors = []
    i = 2

    while n > 1 and i < lim + 1:
        if n%i == 0:
            prime_factors.append(i)
            n = int(n/i)
            
        else:
            i = i + 1
            
    return prime_factors

#%% LCM

factors1 = factorise(n[0])
factors2 = factorise(n[1])

if len(factors1) > len(factors2):
    Gfactors = factors1
    Lfactors = factors2
    
else:
    Gfactors = factors2
    Lfactors = factors1
    
common_factors = 