
__author__ = 'cedric'

from sys import argv

script,user_name,property = argv
prompt = '~~~'

print "Hi %s,I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
print "If you are %s, i am going to give you a hit." % property
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Where kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright,so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice.
""" % (likes,lives,computer)