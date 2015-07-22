# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from abc import abstractmethod
import numpy as np
import pyglet 
import time

current_milli_time = lambda: int(round(time.time() * 1000))

class Entity: 
    """
        The base class for any object inside the game.
    """ 
    
    def __init__(self, identifier="", description="", size=np.array([0.0, 0.0]), pos=np.array([0.0, 0.0]), parent=None, expires=False,
            isChild=False, deathTime=0, renderable=True, interactable=True):
        # (Hopefully) unique identifier for this entity
        self.identifier=""
        # Generic description of what this entity is for. 
        self.description=""
        # Axis-aligned dimensions of the entity.
        self.size           = size
        # Loction of the entity. If the entity is a child, this will be relative to the parent.
        self.pos            = pos
        # Parent of ths entity.
        self.parent         = parent
        # Will the entity expire after appearing on screen?
        self.expires        = expires
        # Is this a child of another entity?
        self.isChild        = isChild
        if self.parent == None:
            self.isChild = False
        # Time at which this entity was created.
        self.creationTime   = current_milli_time()
        # Time at which this entity should expire.
        self.deathTime      = self.creationTime + deathTime
        # Is this entity renderable (ie, will it appear on screen?)
        self.renderable     = renderable
        # Is this entity interactable? At this time, this implies it csan be clicked on.
        self.interactable   = interactable
        # An object cannot be created with children. These are added using addChild
        self.children       = []

    @abstractmethod
    def respond(self): pass

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def update(self, dt): pass

    def toString(self):
        return identifier

    def addChild(self, child):
        self.children.append(child)

    def intersect(self, x, y):
        """ 
            Returns true if a given (x,y) pair are within the axis-aligned-bounding-box of the Entity
            x   :   (int) X location to test against
            y   :   (int) Y location to test against
        """
        return abs(self.pos[0] - x) <= self.size[0] and abs(self.pos[1] - y) <= self.size[1]

class Popup(Entity):
    """
        Temp child class for testing
    """

    def __init__(self, text, identifier="", description="", ox=0.0, oy=0.0, parent=None, expires=True,
            isChild=False, deathtime=3000, renderable=True, interactable=False, fsize=10):
        size    = np.array([0.0, 0.0])
        pos     = np.array([ox+parent.pos[0], oy+parent.pos[1]])
        
        Entity.__init__(self, identifier, description, size, pos, parent, expires, isChild, deathtime, renderable, interactable)
        
        # Fontsize of tjhe popup's message
        self.fsize  = fsize
        self.text   = text
        
    def draw(self):
        label = pyglet.text.Label(self.text,
                    font_name='Times New Roman',
                    font_size=self.fsize,
                    color=(255,0,0,255),
                    x=self.pos[0], y=self.pos[1],
                    anchor_x='center', anchor_y='center')
        label.draw()



        
class Actor(Entity):
    """
        Base class for any moving actor within the game.
        The assumption is that any moving actor can die.
    """
    #sprite = "" 
    alive = True
    description = "A moving actor of unknown particulars"

    def __init__(self, identifier="", description="", sx=0, sy=0, x=0, y=0, vx=0, vy=0, parent=None, expires=False,
            isChild=False, deathtime=0, renderable=True, interactable=True):
        size    = np.array([sx, sy], dtype = 'float32')
        pos     = np.array([x, y], dtype = 'float32')
        Entity.__init__(self, identifier, description, size, pos, parent, expires, isChild, deathtime, renderable, interactable)
        
        # The velocity of the actor
        self.vel = np.array([vx,vy])

    # def __init__(self, identifier, x, y, sx, sy, parent=None):
    #     self.identifier = identifier
    #     self.pos[0]     = x
    #     self.pos[1]     = y
    #     self.size[0]    = sx
    #     self.size[1]    = sy
    #     if parent != None:
    #         self.isChild = True
    #         self.parent = parent
       
    def respond(self):
        """
            This is the (temp) method for when the actor is clicked on
            If the actor is not interactable, do nothing
        """
        if not self.interactable:
            return
        if len(self.children) == 0:
            self.addChild(Popup(text="hi",ox=10,oy=10,fsize=10,parent=self))
    
    def update(self, dt):
        """
            Update the actor's position. 
            Check if this actor has any children that have expired, and if so, kill them.
        """
        self.pos += dt*self.vel     
        
        # Inefficient, but will work for now.
        deleteChildren = []
        for ent in self.children:
            if ent.expires and current_milli_time() >  ent.deathTime:
                deleteChildren.append(ent)
            else:
                ent.pos += dt*self.vel 
        self.children = [e for e in self.children if e not in deleteChildren]

    def setVelocity(self, vx, vy, absolute=False):
        self.vel[0] = vx
        self.vel[1] = vy

        if self.isChild and not absolute:
            self.vel += self.parent.vel

    def updatePosition(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

        if self.isChild and not absolute:
            self.vel += self.parent.vel
    
    def setPosition(self, dx, dy, absolute=False):
        self.pos[0] += dx
        self.pos[1] += dy

        if self.isChild and not absolute:
            self.vel += self.parent.vel
    
    def kill(self):
        self.alive = False
    

    def draw(self):
        if not self.renderable:
            return
        x = int(self.pos[0])
        y = int(self.pos[1])

        if self.isChild:
            x += int(self.parent.pos[0])
            y += int(self.parent.pos[1])

        dx = int(self.size[0])
        dy = int(self.size[1])
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 0, 2, 3], ('v2i', (x, y, x+dx, y, x+dx, y+dy, x, y+dy))) 

        for ent in self.children:
            ent.draw()

class Trap(Entity):
    """ 
        Base class for inanimate, interactable objects
    """
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
        