#!/usr/bin/env python3

n = int(input())
factor = 2
factors = 0
while n > 1:
    if n % factor != 0:
        
        factor = factor + 1
    else:
        factors = factors + 1
        n = n // factor
print(factors)
