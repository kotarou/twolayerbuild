from entity import Component

class UI(Component):
    __slots__ = "active", "visible"
    def __init__(self, maxHp):
        super().__init__()
        self.active = False
        self.visible = False

    def setActive(self, activeIn):
        active = activeIn

    def setVisible(self, visibleIn):
        visible = visibleIn

    def isActive(self):
        return active

    def isVisible(self):
        return visible

    def activate(self):
        pass
