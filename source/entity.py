# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from abc import ABCMeta, abstractmethod

class Entity:
    __metaclass__ = ABCMeta
    
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    @abstractmethod
    def respond(self):
        print("Ouch")
        
class Actor(Entity):
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("Owie")
        
class Trap(Entity):
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("I am a trap")
        
class Object(Entity):
    name = ""
    description = ""
    identifier = ""
    
    def __init__(self, identifier):
        self.identifier = identifier
        
    def respond(self):
        print("I am an object")
        