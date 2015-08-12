# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from entity import Component
from pyglet.window import key
from .KeyComponent import *

class KeyPressComponent(KeyComponent):

    # def __init__(self, key, string="Whatever!"):
    #     self.response = string
    #     self.key = key
    #     self.hoverTime = 0
    #     self.active = False

    def __init__(self, actions):
        super().__init__()
        self.actions = actions
        self.active = False

    def respond(self, input):
        self.parse(self.actions[input])
        #print(self.response)
