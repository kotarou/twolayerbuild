# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from color import *
from util import Vector
import components


#from ecs.models import Component, System, Entity
#from ecs.managers import EntityManager, SystemManager
#from ecs.exceptions import NonexistentComponentTypeForEntity

class Entity(object):
    """
        An object
        It may be better to split this into baseentity and entity to avoid component vs not component logic
        However, for now it is useful to have components and non-components identical
    """
    def __init__(self, eman=None):
        self.color = Color.next()
        if eman is None:
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
        component.attach()

    #def addSimpleMeshComponent(self, )

    def getComponentsByType(self, cType):
        return self.eman.componentsByType(self, cType)

    def getSingleComponentByType(self, cType):
        return self.eman.singleComponentByType(self, cType)

class System(object):
    """
        A system controls the tick logic for components in the game
        For example, an entity with a health component will lose / gain health in two ways
            1) When the component is directly accessed
            2) When the health system updates it
        Interaction logic should not be controlled by a system, unless we move to a update queue.
    """

    def __init__(self):
        # The managers will be added when this system is added to a manager
        self.eman = None
        self.sman = None

    def update(self, _):
        """
            Update method that will be called each tick.
            A system will be added to a manager with an id that determines when in each tick it updates
        """
        raise NotImplementedError("System classes must implment update")

class Component(Entity):
    def __init__(self):
        self.color = Color.next()
        self.owner = None

    def attach(self):
        """
            Init code that requires the owner to have been specified
        """
        pass

class tempClass3(Entity):
    def __init__(self, eman):
        super().__init__(eman)
