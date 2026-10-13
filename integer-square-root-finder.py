#!/usr/bin/env python3

n = int(input())
root = 0
while (root * root) < n:
    root = root + 1
print(root - 1)
