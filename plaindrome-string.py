#!/usr/bin/env python3

n = input()
palindrome = True

while len(n) > 1:
    if n[0] == n[-1]:
        n = n[1:-1]
    else:
        palindrome = False
        break

print(palindrome)
