#!/usr/bin/env python3

n = int(input())
mx = n
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    
    if n > mx:
        mx = n
print(mx)
