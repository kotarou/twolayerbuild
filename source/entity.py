# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
import numpy as np
from color import *
import pyglet.graphics as pg
from pyglet.gl import *

import ctypes

#from ecs.models import Component, System, Entity
#from ecs.managers import EntityManager, SystemManager
#from ecs.exceptions import NonexistentComponentTypeForEntity

class Entity(object):
    """
        An object
        It may be better to split this into baseentity and entity to avoid component vs not component logic
        However, for now it is useful to have components and non-components identical
    """
    def __init__(self, color, eman=None):
        self.color = color
        if eman == None:
            self._isComponent = True
        else:
            self._isComponent = False
        self.eman = eman
        self.components = {}

    @property
    def cid(self):
        return int(self.color.r+self.color.g*255+self.color.b*255*255)

    @property
    def isComponent(self):
        return self._isComponent

    def addComponent(self, component):
        if self._isComponent:
            raise Exception("Components cannot have a component added to them")
        self.eman.addComponent(self, component)

    def getComponents(self):
        if self._isComponent:
            return {}
        else:
            # Currently unimplemented
            return {}
        # r = {}
        # for component in self.eman.database:
        #     for cls in self.eman.database[component]:
        #         if cls.color == self.color:
        #             x = self.eman.database[component][cls]
        #             r[type(x)] = x
        # return r

class System(object):

    def __init__(self):
        # The managers will be added when this system is added to a manager
        self.eman = None
        self.sman = None

    def update (self, _):
        raise NotImplementedError("System classes must implment update")

class Component(Entity):

    def __init__(self):
        self.color = Color.next()
        self.owner = None



class tempClass3(Entity):
    def __init__(self, color, eman):
        super().__init__(color, eman)

