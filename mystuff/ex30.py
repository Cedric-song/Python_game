# -*- coding=utf-8 -*-
__author__ = 'cedric'

people = 30
cars = 40
buses = 15

if cars > people: # means 如果
    print "We should take the cars."
elif cars < people: # means 还如果
    print "We should not take the cars."
else: # means 其他如果
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print "Fine,let's stay home then."

if cars > people and buses < cars:
    print"""We should take cars,not buses.
Because car is faster than bus."""
else:
    print "I have no idea which should we take"