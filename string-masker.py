#!/usr/bin/env python3

n = input()
i = 1
while True:
    if len(n) <= 2:
        break
    if i >= len(n) - 1:
        break
    n = n[0:i] + "*" + n[i+1:]
    i = i + 1
print(n)
