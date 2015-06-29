__author__ = 'cedric'


def zhifubao(all_of_money,accounts_of_cards,phone_cost):
    print ("You have all of money is %r") % all_of_money
    print ("You have %d cards") % accounts_of_cards
    print ("You have %r ") % phone_cost

print "No1"
zhifubao(1000,1,100)

print "No2"
aom = 2000
aoc = 2
pc = 200
zhifubao(aom,aoc,pc)

print "No3"
all_of_money = 3000
accounts_of_cards = 3
phone_cost = 300
zhifubao(all_of_money,accounts_of_cards,phone_cost)

print "No4"
zhifubao(2000+2000,2+2,200+200)

print "No5"
zhifubao(aom+all_of_money,aoc+accounts_of_cards,pc+phone_cost)

