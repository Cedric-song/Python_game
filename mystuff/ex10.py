# -*- coding=utf-8 -*-
__author__ = 'cedric'

# \t means \tab ;   \n means \new line
tabby_cat = "\tI'm tabbed in."  # tabby means 平纹, 斑猫
persian_cat = "I'm split\non a line." # persian means 波斯的, 波斯人[语]
backslash_cat = "I'm \\ a \\ cat." # backslash means 反斜杠

fat_cat = '''
I'll do a list.
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#Q3
cat = "I am a big cat %s\n" % "\n\thowever you are bullshit."
dog = "I am a big dog %s\n" % "however you are %s."
bird = "I am a big bird %s\n" % 'however you are %s' % 'bullshit.'
print cat,dog % 'bullshit',bird

#Q4

Q4_1 = "I am a big %r" % '\"bird\"'
Q4_2 = "I am a big %s" % "\"bird\""
print Q4_1
print Q4_2