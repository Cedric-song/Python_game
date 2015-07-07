__author__ = 'cedric'
"""
1 1

2 1
2 2

3 1
3 2
3 3
"""
for a in range(1,4):
    for b in range(1,4):
        if a >= b:
            print a,b
    print