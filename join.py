#!/usr/bin/env python3

from array import array
import sys

def calcul(nb):
    res = nb
    while nb > 0:
        res += nb % 10
        nb //= 10
    return res

def check_join(arr_s1, arr_s2):
    for i in arr_s1:
        for j in arr_s2:
            if i == j:
                return i
    return -1

def ComputeJoinPoint(s1, s2):
    if ((s1 <= 0 or s1 >= 20000000) or (s2 <= 0 or s2 >= 20000000)):
        sys.exit(84)
    arr_s1 = array('i')
    arr_s2 = array('i')
    while (s1 != s2):
        s1 = calcul(s1)
        s2 = calcul(s2)
        arr_s1.append(s1)
        arr_s2.append(s2)
        res = check_join(arr_s1, arr_s2)
        if res != -1:
            break
    if (res <= 0 or res >= 20000000):
        sys.exit(84)
    return res

print(ComputeJoinPoint(471, 492))