# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from ecs.models import Component
from pyglet.window import key
from .KeyComponent import *

class KeyPressComponent(KeyComponent):

    # def __init__(self, key, string="Whatever!"):
    #     self.response = string
    #     self.key = key
    #     self.hoverTime = 0
    #     self.active = False

    def __init__(self, actions):
    	self.actions = actions

    def respond(self, input):
    	self.parse(self.actions[input])
    	#print(self.response)