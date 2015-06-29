__author__ = 'cedric'

from sys import argv

script,filename = argv

txt = open(filename)
print txt.read()
