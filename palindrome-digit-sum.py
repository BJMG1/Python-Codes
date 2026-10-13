#!/usr/bin/env python3

i = 1
biggest = 0
while i <= 10:
    n = int(input())
    if n % 10 == n // 10 ** (len(str(n)) - 1):
        x = n
        while len(str(x)) > 1:
            if x % 10 == x // 10 ** (len(str(x)) - 1):
                x = x % 10 ** (len(str(x)) - 1)
                x = x // 10
            else:
                break
        if len(str(x)) == 1 and n > biggest:
            if x % 2 == 0:
                biggest = n
    i = i + 1
print(biggest)
