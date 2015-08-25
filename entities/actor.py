from entity import Entity
from components import *

class Actor(Entity):
    """
        An Actor is an entity that 'acts' in the game world.
        This means that the entity is not static, and is expected to interact with other game objects
            Note that an object (such as the ground) that is interacted with is not an actor

    """
    def __init__(self, eman, components=None):
        super().__init__(eman)
        for com in components:
            self.addComponent(com)

    def addSVAComponent(self,
                        position=Vector(0,0,0), velocity=Vector(0,0,0), acceleration=Vector(0,0,0),
                        a_position=Vector(0,0,0), a_velocity=Vector(0,0,0), a_acceleration=Vector(0,0,0),
                        bounded=True):
        self.addComponent(SVAComponent(position, velocity, acceleration, a_position, a_velocity, a_acceleration, bounded))
