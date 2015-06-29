# -*- coding=utf-8 -*-
__author__ = 'cedric'

from sys import argv # 从sys中导入argv模组

script,filename = argv # 定义两个参数,script是脚本本身,filename是一个变量参数名

txt = open(filename) #　给变量txt赋值,定义为open函数　

print "Here's your file %r:" % filename #　print a word
print txt.read() # print content of file "txt"

print "Type the filename again:" # print another filename
file_again = raw_input(">") # input the name of a "txt" file

txt_again = open(file_again) # open the txt and put the value into txt_again

print txt_again.read() # print "txt"file