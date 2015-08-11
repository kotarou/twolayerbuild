# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
import numpy as np
#import pyglet 
import pyglet.graphics as pg
from pyglet.gl import *

import ctypes

#from ecs.models import Component, System, Entity
#from ecs.managers import EntityManager, SystemManager
#from ecs.exceptions import NonexistentComponentTypeForEntity

class Entity(object):
    """ 
        An object
    """
    def __init__(self, color, eman):
        self.eman = eman
        self.color = color
        self.components = {}

    @property 
    def cid(self):
        return int(color.r+color.g*255+color.b*255*255)

    def addComponent(self, component):
        self.eman.add_component(self, component) 

    def getComponents(self):
        r = {}
        for component in self.eman.database:
            for cls in self.eman.database[component]:
                if cls.color == self.color:
                    x = self.eman.database[component][cls]
                    r[type(x)] = x
        return r

class tempClass3(Element):
    def __init__(self, color, eman):
        super().__init__(color, eman)

