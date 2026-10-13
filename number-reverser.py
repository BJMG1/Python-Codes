#!/usr/bin/env python3

n = int(input())

total = 0
while n > 0:
    total = total * 10 + n % 10
    n = n // 10
print(total)
