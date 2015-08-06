# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
import numpy as np
#import pyglet 
import pyglet.graphics as pg
from pyglet.gl import *
import time
import ctypes

from ecs.models import Component, System, Entity
from ecs.managers import EntityManager, SystemManager
from ecs.exceptions import NonexistentComponentTypeForEntity

current_milli_time = lambda: int(round(time.time() * 1000))

class Element(Entity):
    """ 
        An object
    """
    def __init__(self, color, eman):
        self.eman = eman
        self.color = color
        super().__init__(int(color.r*255*255+color.g*255+color.b))

    def addComponent(self, component):
        self.eman.add_component(self, component) 

class tempClass3(Element):
    def __init__(self, color, eman):
        super().__init__(color, eman)

