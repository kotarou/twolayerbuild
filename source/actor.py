# -*- coding: utf-8 -*-
"""
@author: Till
"""

# this will represent a creature or possibly an item or other object that sits on a tile

class actor:


    def __init__(self, identifier, posx, posy):
      self.identifier = identifier
      self.posx = posx
      self.posy = posy

      # Tile it is standing on
      self.location = None
