# -*- coding=utf-8 -*-
__author__ = 'cedric'
"""
抽奖程序
"""


import random
from random import randint
from sys import exit

global TIMES
TIMES = 0
first_award = "一等奖"
second_award = "二等奖"
third_award = "三等奖"
lose_awards = ["So Sad!未中奖",'菜狗,还能不能行','妹子要加油了']
user_list = ['001','002']
black_user_list = ['007']

def start_words():
    print "版本：Edition 1"
    print """这是一个抽奖系统,用户输入"抽奖",即可进行抽奖.
学习python20多天了,这是我自己独立写的第一个程序.
想往这个程序里加入更多的元素,但是目前看来还不好加.
我会不断的更新这个程序的版本,直到写出我想要的.
"""
    return user_data()

def user_data():
    user_id = raw_input("用户名：")
    if user_id in user_list:
        print "身份验证成功"
        return choujiang_times()
    elif user_id in black_user_list:
        print "非法用户,已加入黑名单,赶紧来自首"
        user_data()
    else:
        print "用户不存在"
        return user_data()

def choujiang_times():
    global  TIMES
    print "你今天还可以抽奖%d次." % (3-TIMES)
    TIMES = TIMES + 1
    return TIMES

def choujiang():
    get_num = random.randint(1,100)
    if get_num == 1:
        print first_award

    elif get_num in range(2,4):
        print second_award

    elif get_num in range(4,7):
        print third_award

    else:
        print lose_awards[randint(0,len(lose_awards)-1)]

    return user_input()

def user_input():

    start_program = raw_input("请输入> ")

    if start_program == "抽奖":
        return choujiang()

    else:
        print "请输入：“抽奖”，否则无法抽奖"
        return user_input()







def start_pro():
    global  TIMES
    if TIMES <= 3:
        return user_input()

    else:
        print "今天的抽奖用完了！"
        exit()

start_words()