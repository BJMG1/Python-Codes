#!/usr/bin/env python3

n = int(input())
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10

if total % 2 == 0:
    print(True)
else:
    print(False)
