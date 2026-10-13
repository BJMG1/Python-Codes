#!/usr/bin/env python3

n = input()

if len(n) >= 3:
    n = n[-1] + n[0:-1]

print(n)
