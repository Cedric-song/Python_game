__author__ = 'cedric'
def while_loop(a):
    i = 0
    numbers = []

    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now:",numbers
        print "At the bottom i is %d" % i

    print "The numbers:"

    for num in numbers:
        print num

print while_loop(9)

