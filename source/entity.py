# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from abc import ABCMeta, abstractmethod
import pyglet 

class Entity:  
    name = ""
    description = ""
    identifier = ""
        
    @abstractmethod
    def respond(self): pass

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def update(self, dt): pass
        
class Actor(Entity):
    sprite = "" 
    
    name = ""
    description = ""
    identifier = ""

    def __init__(self, identifier, x, y):
        self.identifier = identifier
        self.x = x
        self.y = y

    x = 0
    y = 0
    
    alive = True    
           
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
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 0, 2, 3], ('v2i', (self.x, self.y,self.x+50, self.y, self.x+50, self.y+50, self.x, self.y+50)))        

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
        