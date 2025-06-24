#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    nums = []
    for i in range(num1, num2 + 1):
        nums.append(i)
    print(nums)