# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
import numpy as np
#import pyglet 
import pyglet.graphics as pg
from pyglet.gl import *
import time

current_milli_time = lambda: int(round(time.time() * 1000))


    # def __cmp__(self, other):
    #     # This defines the order of objects in the depth buffer
    #     return cmp(self.depth, other.depth)

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

    def draw(self):
        pass
    
    def fobDraw(self):
        pass

    def update(self):
        pass

    def colorCompare(self, other):
        return self.handle[0] == other[0] and self.handle[1] == other[1] and self.handle[2] == other[2] 

class MouseInteractable(Element):

    hoverTime = 0.5

    def onClick(self, x, y):
        pass

    def onHover(self):
        pass

class KeyInteractable(Element):

    def onKey(key, modifier):
        pass

class tempClass(MouseInteractable):
    def __init__(self, handle, color):
        self.handle = handle
        self.color  = color

    def onClick(self, x, y):
        print("Temp class!")

    def draw(self):
        glColor3ub(self.color[0], self.color[1], self.color[2])
        glVertex3f(-50  , -50   , 10)
        glVertex3f(-50  , 50    , 10)
        glVertex3f(50   , 50    , 10)
        glVertex3f(50   , -50   , 10.0)

    def fboDraw(self):
        glColor3ub(self.handle[0], self.handle[1], self.handle[2])
        glVertex3f(-50  , -50   , 10)
        glVertex3f(-50  , 50    , 10)
        glVertex3f(50   , 50    , 10)
        glVertex3f(50   , -50   , 10.0)

    def update(self):
        x = 3

class tempClass2(MouseInteractable):
    def __init__(self, handle, color):
        self.handle = handle
        self.color  = color

    def onClick(self, x, y):
        print("Temp class2!")

    def draw(self):
        glColor3ub(self.color[0], self.color[1], self.color[2])
        glVertex3f(-30  , -30   , 0)
        glVertex3f(-30  , 30    , 0)
        glVertex3f(30   , 30    , 0)
        glVertex3f(30   , -30   , 0.0)

    def fboDraw(self):
        glColor3ub(self.handle[0], self.handle[1], self.handle[2])
        glVertex3f(-30  , -30   , 0)
        glVertex3f(-30  , 30    , 0)
        glVertex3f(30   , 30    , 0)
        glVertex3f(30   , -30   , 0.0)

    def update(self):
        x = 3

class tempClass3(MouseInteractable):
    def __init__(self, handle, color):
        self.handle = handle
        self.color  = color

    def onClick(self, x, y):
        print("Temp class3!")

    def draw(self):
        glColor3ub(self.color[0], self.color[1], self.color[2])
        glVertex3f(-10  , -10   , -10)
        glVertex3f(-10  , 10    , -10)
        glVertex3f(10   , 10    , -10)
        glVertex3f(10   , -10   , -10.0)

    def fboDraw(self):
        glColor3ub(self.handle[0], self.handle[1], self.handle[2])
        glVertex3f(-10  , -10   , -10)
        glVertex3f(-10  , 10    , -10)
        glVertex3f(10   , 10    , -10)
        glVertex3f(10   , -10   , -10.0)

    def update(self):
        x = 3

# class Entity: 
#     """
#         The base class for any non-menu element inside the game.

#         Required parameters
#         identifier (string) :   A unique handle for identifying am entity. Will be used to index the entity in the game world.

#         Optional parameters
#         description (string):   A string that describes the entity. Will be revealed when the entities toString() method is called.
#                                 Must be defined if the object is interactable
#         size (1x2 np array) :   The dimensions (x,y) of the axis-aligned bounding box of the entity.
#         pos (1x2 np array)  :   The position of the top left corner of this entities axis-aligned bounding box in screen space.
#         parent (reference)  :   The parent of this entities. If this is defined, the entity will inherit transformations from the parent.
#         expires (bool)      :   Whether the entity will expire and be deleted.
#         deathtime (float)   :   The time in milliseconds that the entity will expire at.
#         renderable (bool)   :   Whether the entity will be rendered or not.
#         interactable (bool) :   Whether the entity will respond to player interaction or not. 
#     """ 
    
#     def __init__(self, 
#             identifier, description="", 
#             size=np.array([0.0, 0.0]), pos=np.array([0.0, 0.0]), 
#             parent=None, 
#             expires=False, deathTime=0, 
#             renderable=True, interactable=True):
#         # (Hopefully) unique identifier for this entity
#         self.identifier     = identifier
#         # Generic description of what this entity is for. 
#         self.description    = description
#         # Axis-aligned dimensions of the entity.
#         self.size           = size
#         # Loction of the entity. If the entity is a child, this wll intially be the offest of the child against the parent.
#         self.pos            = pos
#         # Parent of ths entity.
#         self.parent         = parent
#         # Will the entity expire after appearing on screen?
#         self.expires        = expires
#         # Is this a child of another entity?
#         if self.parent == None:
#             self.isChild = False
#         else:
#             self.isChild=True
#         # Time at which this entity was created.
#         self.creationTime   = current_milli_time()
#         # Time at which this entity should expire.
#         self.deathTime      = self.creationTime + deathTime
#         # Is this entity renderable (ie, will it appear on screen?)
#         self.renderable     = renderable
#         # Is this entity interactable? At this time, this implies it csan be clicked on.
#         self.interactable   = interactable
#         if self.interactable and len(self.description) == "":
#             print("An entity must have a description if it can be interacted with")
#             raise Exception(self.identifier, "Interactable object with no description")
#         # An object cannot be created with children. These are added using addChild
#         self.children       = []

#     @abstractmethod
#     def respond(self): pass

#     @abstractmethod
#     def draw(self): pass

#     @abstractmethod
#     def update(self, dt): pass

#     def toString(self):
#         return ("Entity:", self.identifier, "with description:", self.description)

#     def addChild(self, child):
#         self.children.append(child)

#     def intersect(self, x, y):
#         """ 
#             Returns true if a given (x,y) pair are within the axis-aligned-bounding-box of the Entity
#             x   :   (int) X location to test against
#             y   :   (int) Y location to test against
#         """
#         return abs(self.pos[0] - x) <= self.size[0] and abs(self.pos[1] - y) <= self.size[1]

# class Popup(Entity):
#     """
#         Temp child class for testing
#         It does not make sense for a popup to need a description to be added.

#     """

#     def __init__(self, text, identifier, description="", ox=0.0, oy=0.0, parent=None, expires=True,
#             deathtime=3000, renderable=True, interactable=False, fsize=10):
#         size    = np.array([0.0, 0.0])
#         pos     = np.array([ox+parent.pos[0], oy+parent.pos[1]])
        
#         Entity.__init__(self, identifier, description, size, pos, parent, expires, deathtime, renderable, interactable)
        
#         # Fontsize of the popup's message
#         self.fsize  = fsize
#         self.text   = text
        
#     def draw(self):
#         label = pyglet.text.Label(self.text,
#                     font_name='Times New Roman',
#                     font_size=self.fsize,
#                     color=(255,255,255,255),
#                     x=self.pos[0], y=self.pos[1],
#                     anchor_x='center', anchor_y='center')
#         label.draw()

#     def update(self, dt):
#         self.pos = self.pos + self.parent.vel*dt
     
# class Actor(Entity):
#     """
#         Base class for any interactive actor within the game.
        
#         Required parameters:
#         description (string):   Unlike the base Entity, an actor is always going to be interactive, and thus always needs a descrption.
#                                 The interactable arguement allows a actor to be loaded before it can be interacted with.

#         Optional parameters:
#         color (f, f, f)     :   A color arguement to control the color of the basic square representing the actor.
#                                 Will be removed once sprite loading is possible.
#         sx, sy (float)      :   The size (horixontal, vertical) of the actor 
#         x, y (float)        :   The position of the actor in screen space, relative to its parent (if any)
#         vx, vy (float)      :   The velocity of the actor in screen space, relative to its parent (if any)
#     """
#     #sprite = "" 
#     alive = True
#     description = "A moving actor of unknown particulars"

#     def __init__(self, identifier, description, sx=0, sy=0, x=0, y=0, vx=0, vy=0, parent=None, expires=False,
#             deathTime=0, renderable=True, interactable=True, color=(1.0,1.0,1.0)):
#         size    = np.array([sx, sy], dtype = 'float32')
#         pos     = np.array([x, y], dtype = 'float32')
#         Entity.__init__(self, identifier, description, size, pos, parent, expires, deathTime, renderable, interactable)
        
#         # The velocity of the actor
#         self.vel = np.array([vx,vy])
#         if self.isChild:
#             self.vel += parent.vel

#         # If this is a child, define its location by adding its position(offset) to its parents
#         if self.isChild:
#             self.pos = parent.pos + self.pos

#         # The color of the actor
#         self.color = color

#     # def __init__(self, identifier, x, y, sx, sy, parent=None):
#     #     self.identifier = identifier
#     #     self.pos[0]     = x
#     #     self.pos[1]     = y
#     #     self.size[0]    = sx
#     #     self.size[1]    = sy
#     #     if parent != None:
#     #         self.isChild = True
#     #         self.parent = parent
       
#     def respond(self):
#         """
#             This is the (temp) method for when the actor is clicked on
#             If the actor is not interactable, do nothing
#         """
#         if not self.interactable:
#             return
#         #Wif len(self.children) == 2:
#         self.addChild(Popup(identifier="popup",text="hi",ox=10,oy=10,fsize=10,parent=self,interactable=False))
    
#     def update(self, dt):
#         """
#             Update the actor's position. 
#             Check if this actor has any children that have expired, and if so, kill them.
#         """
#         self.pos += dt*self.vel     
        
#         # Inefficient, but will work for now.
#         deleteChildren = []
#         for ent in self.children:
#             if ent.expires and current_milli_time() >  ent.deathTime:
#                 deleteChildren.append(ent)
#             else:
#                ent.update(dt)
#         self.children = [e for e in self.children if e not in deleteChildren]

#     # def setVelocity(self, vx, vy, absolute=False):
#     #     self.vel[0] = vx
#     #     self.vel[1] = vy

#     #     if self.isChild and not absolute:
#     #         self.vel += self.parent.vel

#     # def updatePosition(self, dx, dy):
#     #     self.pos[0] += dx
#     #     self.pos[1] += dy

#     #     if self.isChild and not absolute:
#     #         self.vel += self.parent.vel
    
#     # def setPosition(self, dx, dy, absolute=False):
#     #     self.pos[0] += dx
#     #     self.pos[1] += dy

#     #     if self.isChild and not absolute:
#     #         self.vel += self.parent.vel
    
#     # def kill(self):
#     #     self.alive = False
    

#     def draw(self):
#         if not self.renderable:
#             return
#         x = int(self.pos[0])
#         y = int(self.pos[1])

#         # if self.isChild:
#         #     x += int(self.parent.pos[0])
#         #     y += int(self.parent.pos[1])

#         dx = int(self.size[0])
#         dy = int(self.size[1])
#         pyglet.gl.glColor3f(self.color[0],self.color[1],self.color[2]); 
#         pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 0, 2, 3], ('v2i', (x, y, x+dx, y, x+dx, y+dy, x, y+dy))) 

#         for ent in self.children:
#             ent.draw()

# class Trap(Entity):
#     """ 
#         Base class for inanimate, interactable objects
#     """
#     name = ""
#     description = ""
#     identifier = ""
    
#     location = ""
        
#     def __init__(self, identifier):
#         self.identifier = identifier
        
#     def respond(self):
#         print("I am a trap")
        
#     def activate(self, target):
#         print("BANG")
            
        
# class Object(Entity):
#     name = ""
#     description = ""
#     identifier = ""
    
#     def __init__(self, identifier):
#         self.identifier = identifier
        
#     def respond(self):
#         print("I am an object")
#         