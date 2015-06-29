# -*- coding=utf-8 -*-
__author__ = 'cedric'

x = "There are %d types of people." % 10 #　%后可以直接跟值
binary = "binary" # binary means 二进制
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said:%r." % x # 输出ｘ，ｘ是一个字符串，%r为原文输出。
print "I also said:'%s'." % y # 输出ｙ，ｙ被定义为一个字符串。

hilarious = False # hilarious means a. 喜不自禁的, 欢闹的, 引人发笑的
joke_evaluation = "Isn't that joke so funny?! %r" # evaluation means 评价,估价

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print w + joke_evaluation % hilarious
'''n

    '''

# Q1添加注释　
# Q2字符串包含字符串　
''' 1.y = "Those who know %s and those who %s." % (binary,do_not)
    2.print "I said:%r." % x
    3.joke_evaluation = "Isn't that joke so funny?! %r"
    4.print joke_evaluation % hilarious
    5.print "I said:%r."
    6.print "I also said:'%s'." % y
    '''
# Q3 6个
# Q4 +可以用来连接字符串