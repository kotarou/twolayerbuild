from entity import Component

class UI(Component):
    __slots__ = "active", "visible", "name"
    def __init__(self, nameIn):
        super().__init__()
        self.active = False
        self.visible = False
        self.name = nameIn

    def setActive(self, activeIn):
        active = activeIn

    def setVisible(self, visibleIn):
        visible = visibleIn

    def getActive(self):
        return active

    def getVisible(self):
        return visible

    def getName(self):
        return name

    def activate(self):
        pass
