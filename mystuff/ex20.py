# -*- coding=utf-8 -*-
__author__ = 'cedric'

from sys import argv #导入元组argv

script,input_file = argv #定义参数

def print_all(f): #定义函数
    print f.read() #打印参数f读取的内容

def rewind(f): #定义函数rewind
    f.seek(0) #从内容第０位开始搜寻

def print_a_line(line_count,f): #定义函数print_a_line,两个参数
    print line_count,f.readline() #打印line_count和f的某一行

current_file = open(input_file) # current_file 被赋值为input_file的文件内容

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)