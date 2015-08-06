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

class Element(object):
    """ 
        An object
    """

    def __init__(self, handle):
        """
        glColor3f handle
        """
        # An object should have a unique handle
        self.handle = handle

class tempClass3(Entity):
    def __init__(self, color, eman):
        self.eman = eman
        self.color = color
        super().__init__(int(color.r*255*255+color.g*255+color.b))

