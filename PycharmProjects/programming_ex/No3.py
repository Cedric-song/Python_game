# -*- coding=utf-8 -*-
__author__ = 'cedric'
"""
1 1

1 2
2 2

1 3
2 3
3 3
"""

for a in range(1,4):
    for b in range(1,a+1):
        print b,a

    print

# 第二种方法
for m in range(1,4):
    for n in range(1,4):
        if m >= n:
            print n,m
    print