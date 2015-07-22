# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from abc import ABCMeta, abstractmethod
import numpy as np
import pyglet 

class Entity: 
    """
        The base class for any object inside the game.
    """ 
    name = ""
    description = ""
    identifier = ""
    
    renderable = True
    interactable = True

    @abstractmethod
    def respond(self): pass

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def update(self, dt): pass

    def toString(self):
        return identifier    
        
class Actor(Entity):
    """
        Base class for any moving actor within the game.
        The assumption is that any moving actor can die.
    """
    sprite = "" 
    pos = np.array([0.0,0.0])
    vel = np.array([0.0,0.0])
    alive = True
    description = "A moving actor of unknown particulars"

    def __init__(self, identifier, x, y):
        self.identifier = identifier
        self.pos[0] = x
        self.pos[1] = y
       
    def respond(self):
        print("Owie")
    
    def update(self, dt):
        self.pos += dt*self.vel

    def setVelocity(self, vx, vy):
        self.vel[0] = vx
        self.vel[1] = vy

    def updatePosition(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy
    
    def setPosition(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
    
    def kill(self):
        self.alive = False
                
    def draw(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 0, 2, 3], ('v2i', (x, y,x+50, y, x+50, y+50, x, y+50)))        

class Trap(Entity):
    name = ""
    description = ""
    identifier = ""
    
    location = ""
        
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("I am a trap")
        
    def activate(self, target):
        print("BANG")
            
        
class Object(Entity):
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("I am an object")
        