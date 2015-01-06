# Exercise 45: You Make A Game

'''
It's a very simple example of a "text-based game",
where you can go to one room or another.
It uses classes, inheritance and composition.
Of course, it can be improved or extended in the future.
'''

class Game(object):
  def __init__(self):
    self.kitchen = Kitchen()
    self.living_room = LivingRoom()

  def start(self):
    print "starting game..."
    action = raw_input("choose room: ")
    if action == "kitchen":
      self.kitchen.enter()
    elif action == "living_room":
      self.living_room.enter()
    else:
      print "I don't know that place"

class Room(object):
  def enter(self):
    pass

  def leave(self):
    print "leaving room"

class Kitchen(Room):
  def enter(self):
    print "entering Kitchen..."

class LivingRoom(Room):
  def enter(self):
    print "entering Living Room..."

game = Game()
game.start()
