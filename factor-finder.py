#!/usr/bin/env python3

n = int(input())
start = n
divisors = 0
factor = 1
factors = []
while factor <= n:
    if n % factor == 0:
        divisors = divisors + n // factor + factor
        if not factor in factors:
            factors.append(factor)
        factor = factor + 1
    else:
        factor = factor + 1

print(factors)