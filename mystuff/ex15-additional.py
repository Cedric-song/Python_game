# -*- coding=utf-8 -*-
__author__ = 'cedric'
# Q5
filename = raw_input("type your file's name:")
print "Here's your file %r:" % filename
txt = open(filename)
print txt.read()


