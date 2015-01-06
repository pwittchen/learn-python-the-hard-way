# Exercise 40: Modules, Classes, and Objects - part 1

'''
# dictionary example
mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

# modules are like dictionaries

# this goes in mystuff.py
def apple():
    print "I AM APPLES!"

# accessing module

import mystuff
mystuff.apple()

# updated module

def apple():
    print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream"

# accessing module

import mystuff

mystuff.apple()
print mystuff.tangerine

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

# classes are like modules - go to exercise40_2.py

'''
