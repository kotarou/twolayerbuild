from game import world
from components import *
from entity import *
class UI:

    self.uiActorList = []
    self.visibleMode = False
    self.currentlySelectedUIElement = None

    def __init__(self):
        x = Actor(game.world.EntityManager) # the esc to/from menu interaction
        x.addComponent(KeyPressComponent({key(key.ESC, 0): toggleVisible()}))
        uiActorList.append(x)

        createUIActor(MeshComponent(shape = Rectangle(50, 100, Vector(-100, 0, 0), BOTTOMLEFT, [Color(100, 100, 100)*4], None)), "Start Game")
        createUIActor(MeshComponent(shape = Rectangle(50, 100, Vector(100, 0, 0), BOTTOMLEFT, [Color(100, 100, 100)*4], None)), "Quit Game")

    def createUIActor(self, meshComponentIn, nameIn):

        x = Actor(game.world.EntityManager)

        x.addComponent(meshComponentIn)
        x.addComponent(UIComponent(nameIn))

        x.addComponent(KeyPressComponent({key(key.UP, 0): [self.setActiveUIActor(currentlySelectedUIElement, -1)]})) # moves to the above menu element
        x.addComponent(KeyPressComponent({key(key.DOWN, 0): [self.setActiveUIActor(self.currentlySelectedUIElement, 1)]})) # moves to the below menu element
        x.addComponent(KeyPressComponent({key(key.ENTER, 0): [activate(self.currentlySelectedUIElement)]})) # do stuff to this element (keyboard)

        x.addComponent(MouseClickComponent(activate(self.currentlySelectedUIElement))) # do stuff to this element (mouse)
        x.addComponent(MouseHoverComponent(self.setActiveUIActorByMouse(self.currentlySelectedUIElement, owner)) # moves to the hovered element

        uiActorList.append(x)

    def toggleVisible(self):
        self.visibleMode = !self.visibleMode
        for x in uiActorList:
            x.getSingleComponentsByType(UIComponent).setVisible(self.visibleMode)

    def activate(self, currentUIActor):
        if(currentUIActor.getSingleComponentsByType(UIComponent).getName() == "Start Game"):
            game.startGame()
        elif(currentUIActor.getSingleComponentsByType(UIComponent).getName() == "Quit Game"):
            game.endGame()

    def setActiveUIActor(self, currentUIActor, offset):
        temp = self.uiActorList.index(currentUIActor)
        currentUIActor.getSingleComponentsByType(UIComponent).setActive(False)
        if((temp + offset) > self.uiActorList.size()):
            self.uiActorList.get(0).getSingleComponentsByType(UIComponent).setActive(True)
        elif(0 > (temp + offset)):
            self.uiActorList.get(self.uiActorList.size()).getSingleComponentsByType(UIComponent).setActive(True)
        elif(True):
            self.uiActorList.get(temp + offset).getSingleComponentsByType(UIComponent).setActive(True)

    def setActiveUIActorByMouse(self, currentUIActor, newUIACtor):
        currentUIActor.getSingleComponentsByType(UIComponent).setActive(False)
        newUIACtor.getSingleComponentsByType(UIComponent).setActive(True)
