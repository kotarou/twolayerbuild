from entity import Entity
from util import *
from components import *
from pyglet.window import key

class Limb(Entity):
    """
        A limb of an Actor
        Contains a mesh and a collision component
    """
    def __init__(self, eman, mesh):
        super().__init__(eman)

        self.addComponent(mesh)
        self.addComponent(CollisionComponent("limb", ["weapon"], useAABB=False, AABB=None, collidable=True))
        self.addComponent(SVAComponent())


class Actor(Entity):
    """
        An Actor is an player controlled entity.
        Actors the following Limbs:
            Head
            L Arm
            R Arm
            L Leg
            R Leg
            Body

    """
    def __init__(self, eman):
        super().__init__(eman)
        # Head
        self.head = Limb(eman,
                         MeshComponent(shape=Rectangle(10, 30, Vector(50,130, 0), CENTER, [Color(255,255,255)*4], None)))
        # Body
        self.body = Limb(eman,
                         MeshComponent(shape=Rectangle(30, 50, Vector(40,100, 0), TOPLEFT, [Color(255,255,0)*4], None)))
        # Arms
        self.larm = Limb(eman,
                         MeshComponent(shape=Rectangle(20, 30, Vector(40,100, 0), TOPRIGHT, [Color(255,0,0)*4], None)))
        self.rarm = Limb(eman,
                         MeshComponent(shape=Rectangle(20, 30, Vector(70, 100, 0), TOPLEFT, [Color(255,0,255)*4], None)))
        # Legs
        self.lleg = Limb(eman,
                         MeshComponent(shape=Rectangle(20, 50, Vector(30, 50, 0), TOPLEFT, [Color(128,0,255)*4], None)))
        self.rleg = Limb(eman,
                         MeshComponent(shape=Rectangle(20, 50, Vector(60, 50, 0), TOPLEFT, [Color(255,0,128)*4], None)))

        self.addComponent(KeyHoldComponent({Key(key.Q, 0): [
"""
owner.larm.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,1)
""",
"""
owner.larm.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,0)
"""
]}))
        self.addComponent(KeyHoldComponent({Key(key.W, 0): [
"""
owner.rarm.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,1)
""",
"""
owner.rarm.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,0)
"""
]}))
        self.addComponent(KeyHoldComponent({Key(key.A, 0): [
"""
owner.lleg.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,1)
""",
"""
owner.lleg.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,0)
"""
]}))
        self.addComponent(KeyHoldComponent({Key(key.S, 0): [
"""
owner.rleg.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,1)
""",
"""
owner.rleg.getSingleComponentByType(SVAComponent).OMEGA = Vector(0,0,0)
"""
]}))

    def addSVAComponent(self,
                        position=Vector(0,0,0), velocity=Vector(0,0,0), acceleration=Vector(0,0,0),
                        a_position=Vector(0,0,0), a_velocity=Vector(0,0,0), a_acceleration=Vector(0,0,0),
                        bounded=True):
        self.addComponent(SVAComponent(position, velocity, acceleration, a_position, a_velocity, a_acceleration, bounded))

    def interact(self, other):
        pass
