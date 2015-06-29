# -*- coding=utf-8 -*-
__author__ = 'cedric'

# 加分习题

''' 1.修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不只是你使用``=``赋值过的地方。
    2.试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。
    3.在网上搜索所有的 Python 格式化字符。
    4.试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。
    '''

# Q1&Q2
name = 'Zed A. shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teech = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d pound heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teech

# this line is tricky,try to get it exactly right
print "If i add %d,%d and %d I get %d. " % (age,height,weight,age+height+weight)

# Q3

# the use of %c
charA = 65
print ('ASCII 65代表：%c' % charA)

''' %r      优先用于repr()函数进行字符串转换
    %s      优先用于str()函数进行字符串转换
    %d/%i   转换成有符号十进制数
    %u      转成无符号十进制数
    %o      转成无符号八进制数
    %x/%X   转成无符号十六进制数
    %e/%E   转成科学计数法
    %f/%F   转成浮点数
    '''

# Q4
my_height = 74 #inches
my_weight = 180 #lbs
my_height_centimeter = my_height * 2.54
my_weight_kilo = my_weight * 0.4536
print "He's %d cm tall." % my_height_centimeter
print "He's %d kg heavy." % my_weight_kilo