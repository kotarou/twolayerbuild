# -*- coding: utf-8 -*-
"""
@author: Till
"""

class Tile:

  def __init__(self, symbol, x, y):

    self.x = x
    self.y = y

    self.texture = 0

    self.above = None
    self.left = None
    self.right = None
    self.below = None

    self.navigatable = True
    self.rooms = []
    self.contents = []

    # set its texture based on character in map
    # also if it is navigatable
    if symbol == "#":
      pass

    elif symbol == "*":
      pass

    elif symbol == ".":
      pass

    elif symbol == "@":
      pass

    else:
      print("oopsy " + symbol)

  def is_adjacent_room(self, room):
      pass

  def is_diag_adjacent_room(self, room):
      pass

  def add_content(self, content):
      pass

  def remove_content(self, identifier):
      pass

  def contains(self, identifier):
      pass
