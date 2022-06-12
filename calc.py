#!/usr/bin/env python3

import sys

def calc(arr, n1, n2):
    sum = 0
    if n1 < 0:
        sys.exit(84)
    if n2 < n1:
        sys.exit(84)
    if len(arr) < n2:
        sys.exit(84)
    for i in arr:
        if i >= n1 and i <= n2:
            sum = sum + i
    return sum
