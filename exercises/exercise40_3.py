# Exercise 40: Modules, Classes, and Objects - part 3

class Song(object):
    my_public_variable = "test public" # variables without any prefix are treated as public
    __my_private_variable = "test private" # variables with prefix __ are trated as private
    _my_protected_variable = "test protected" # variables with prefix _ are treated as protected

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def get_lyrics(self):
      return self.lyrics

    def __my_private_method(self): # methods with prefix __ are treated as private, rest is public; same story as variables above
      print "private stuff"


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
