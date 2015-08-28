from game import world
from components import *

class ui:

    self.uiActorDict = None
    self.visibleMode = False

    def __init__(self):
        createUIActor(MeshComponent(shape=Square(50, Vector(0,0,0), CENTER, [Color(1,1,1)*4], None)))

        x = Actor(game.world.EntityManager)

        x.addComponent(KeyPressComponent({key(key.ESC, 0): for x in self.uiActorDict: x.setVisible(!self.visibleMode)}))
        x.addComponent(KeyPressComponent({key(key.ESC, 0): self.visibleMode = !self.visibleMode}))
        self.uiActorDict.append(x)




    def createUIActor(self, meshComponentIn):

        x = Actor(game.world.EntityManager)

        x.addComponent(meshComponentIn)
        x.addComponent(UIComponent)
        x.addComponent(KeyPressComponent(if(owner.isActive() and owner.isVisible()):({key(key.UP, 0): [owner.getNextUIActor().setActive()]})))) # moves to the above menu element
        x.addComponent(KeyPressComponent(if(owner.isActive() and owner.isVisible()):({key(key.DOWN, 0): [owner.getPreviousUIActor().setActive()]}))) # moves to the below menu element
        x.addComponent(KeyPressComponent(if(owner.isActive() and owner.isVisible()):({key(key.ENTER, 0): [owner.activate()]}))) # do stuff to this element (keyboard)

        x.addComponent(MouseClickComponent(if(owner.isActive() and owner.isVisible()): owner.activate())) # do stuff to this element (mouse)
        x.addComponent(MouseHoverComponent(if(owner.isVisible() and owner.isVisible()): owner.setActive()) # moves to the hovered element

        self.uiActorDict.append(x)

    def getNextUIActor(self, currentUIActor):
        temp = self.uiActorDict.getKey(currentUIActor)
        if(temp + 1 > self.uiActorDict.size()):
            return self.uiActorDict.get(temp+1)
        elif:
            return self.uiActorDict.get(0)

    def getPreviousUIActor(selfm currentUIActor):
        temp = self.uiActorDict.getKey(currentUIActor)
        if(temp - 1 > 0):
            return self.uiActorDict.get(temp-1)
        elif:
            return self.uiActorDict.get(self.uiActorDict.size())
