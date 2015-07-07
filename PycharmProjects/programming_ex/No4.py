__author__ = 'cedric'
"""
1 1
1 2  2 2
1 3  2 3  3 3
1 4  2 4  3 4  4 4
"""

for a in range(1,5):
    for b in range(1,a+1):
        print '%d %d  ' % (b,a),
    print


def gen(line_cnt):
    for row in range(1,line_cnt+1):
        for col in range(1,row+1):
            print '%d %d \t' % (col,row),
        print ''

if __name__ == '__main__':
    gen(4)