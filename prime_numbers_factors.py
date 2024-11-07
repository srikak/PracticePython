# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:10:36 2024

@author: ksrik
"""
#%% Get input
print("Enter an integer below:")
try:
    n = int(input())
    
except:
    print("Not a proper number!\n")

#%% Find factors
factors = [1, n]
lim = int(n*0.5) + 1

for i in range(2, lim):
    
    if n%i == 0:
        factors.append(i)
        factors.append(int(n/i))

factors = sorted(set(factors))
        
if len(factors) > 2:
    print(f"{n} is not a prime number\nFactors = {factors}")

else:
    print(f"{n} is a prime number\nFactors = {factors}")
    