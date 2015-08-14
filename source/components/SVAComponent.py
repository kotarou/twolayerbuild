# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from entity import Component
from util import Vector
from pyglet.window import key

class SVAComponent(Component):
    __slots__ = "S", "V", "A", "THETA", "OMEGA", "ALPHA", "anchor"
    def __init__(self, position=Vector(0,0,0), velocity=Vector(0,0,0), acceleration=Vector(0,0,0),
        a_position=Vector(0,0,0), a_velocity=Vector(0,0,0), a_acceleration=Vector(0,0,0)):#, anchor=Vector(0,0,0)):
        super().__init__()
        # Linear
        self.oldS = position
        self.S = position
        self.V = velocity
        self.A = acceleration
        # Rotational
        # Ie, rotation around x axis, y axis, z axis (euler angles)
        # Very simple, temporary code.
        self.THETA = a_position
        # theta, phi,
        self.OMEGA = a_velocity
        self.ALPHA = a_acceleration

        #self.anchor = anchor

    def respond(self, input):
        self.parse(self.actions[input])
        #print(self.response)

    @property
    def position(self):
        return self.S
    @property
    def velocity(self):
        return self.V
    @property
    def acceleration(self):
        return self.A

