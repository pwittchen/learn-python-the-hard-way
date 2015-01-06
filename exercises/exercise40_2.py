# Exercise 40: Modules, Classes, and Objects - part 2

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine

'''
# Getting Things from Things

# dict style
mystuff['apples']

# module style
import mystuff
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine

'''
