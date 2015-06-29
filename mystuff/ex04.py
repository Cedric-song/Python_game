# -*- coding:utf-8 -*-

cars = 100 
# 有100辆车
space_in_a_car = 4
# 一辆车有4个座位
drivers = 30
# 有30个司机
passengers = 90
# 有90个乘客
cars_not_driven = cars - drivers
# 没开的车=车数-司机数
cars_driven = drivers
# 开的车=司机数
carpool_capacity = cars_driven * space_in_a_car
# 座位总数=开的车数＊一辆车的座位数
average_passengers_per_car = passengers / cars_driven
# 平均每辆车乘客数=乘客数／开的车数


print "There are",cars,"cars available."
print "There are only",drivers,'drivers avaliable.'
print 'There will be',cars_not_driven,'empty cars today.'
print 'We can transport',carpool_capacity,'people today.'
print 'We have',passengers,'to carpool today.'
print 'We need to put about',average_passengers_per_car,'in each car.'


print "average_passengers_per_car = car_pool_capacity / passenger NameError: name 'car_pool_capacity' is not defined"
print '这个报错的意思是car_pool_capacity未定义，原为变量'

print "'='means'equal'","'_'means'underscore'"
