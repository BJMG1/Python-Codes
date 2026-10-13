#!/usr/bin/env python3

n = int(input())
start = n
divisors = 0
factor = 2

while factor < n:
    if n % factor == 0:
        divisors = divisors + n // factor + factor
        print(n // factor,factor)
        factor = factor + 1
    else:
        factor = factor + 1
    
print(divisors)

if divisors // 2 + 1 == start:
    print(True)
else:
    print(False)
