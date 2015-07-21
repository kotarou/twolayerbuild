# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from abc import ABCMeta, abstractmethod
import pyglet 

class Entity:
    __metaclass__ = ABCMeta
    
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    @abstractmethod
    def respond(self): pass

    @abstractmethod
    def draw(self): pass
        
class Actor(Entity):
    sprite = "" 
    
    name = ""
    description = ""
    identifier = ""
    
    posX = 0
    posY = 0
    
    alive = True    
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("Owie")
    
    def updatePosition(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def kill(self):
        self.alive = False
                
    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 0, 2, 3], ('v2i', (100, 100,150, 100, 150, 150, 100, 150)))        

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
        