
__author__ = 'cedric'

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    'So i said "goodnight".'
)


# Q1:i don't have any mistake.

#  Q2:The str will use double quotation marks,when the sentance exist single quotation marks.
