# -*- coding=utf-8 -*-
__author__ = 'cedric'
'''python的open方法中，第一个参数是文件位置和文件名，第二个参数是读写模式。
    w是以写方式打开，文件若存在，首先要清空，然后重新创建。
'''
from sys import argv #　从sys导入模组argv

script,filename = argv # 定义两个参数，script&filename

print "We're going to erase %r." % filename # 打印一句话，格式化字符为filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?") # 用户输入

print "Opening the file..." #打印句子
target = open(filename,'w') # 定义target，为open

print "Truncating the file.Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()