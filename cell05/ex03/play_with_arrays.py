#!/usr/bin/env python3

arr =  [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)
new = set()
for i in arr:
    if i > 5:
        new.add(i+2)
print(new)