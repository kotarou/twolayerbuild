# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""

from entity import Component
from pyglet.window import key
from collections import namedtuple
from .HealthComponent import Health
from .SVAComponent import SVAComponent
from .MeshComponent import MeshComponent
from util import Vector

class Key(namedtuple('__KeyCombination', 'symbol modifiers modMatters')):
    """
        A key + modifying keys combination.
        A Key will register Key(symbol,mod) as being equal to Key(symbol,mod2) so long as mod is a subset of mod2 or vice versa
        This way, random modifiers like numlock will not have an effect on playability.
        This does mean that differentiating ctrl+shift+x and ctrl+x is not currently possible
    """

    s_symbol = 0
    s_modifiers = 0
    s_modMatters = False

    def __new__(cls, symbol, modifiers, modMatters=False):
        return super(Key, cls).__new__(cls, symbol, modifiers, modMatters)

    def __eq__(self, other):
        symbol, modifiers, modMatters = self
        if other is None:
            return False

        #the left is what we want to be pushed (normally) mand the right is what is being pushed (again, normally)

        if symbol == other.symbol:
            if not modMatters or (modifiers & other.modifiers):  # (not modMatters and not other.modMatters)
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        symbol, mod, modMatters = self
        # We do not care about modifiers when testing for presence in a dict / etc
        # Later code will check the modifiers anyway, and it is a small efficiency hit for a few false positives
        return symbol  # * 1000) + (mod * 100) # + (1 if modMatters else 0)

class KeyComponent(Component):

    def __init__(self):
        super().__init__()

    def parse(self, input):
        x = self.owner
        d = globals()
        d["eman"] = x.eman
        d["owner"] = x
        d["SVAComponent"] = SVAComponent
        d["MeshComponent"] = MeshComponent
        d["Vector"] = Vector
        exec(input, globals(), d)


if __name__ == "__main__":
    """
        Testing if I haven't broken anything.
    """
    print("Construct a key and print its symbol by calling its name. Should be 97")
    print(Key(key.A, 0, False).symbol)
    print("Construct a key and print its symbol by calling its tuple position. Should be 98")
    print(Key(key.B, 0, False)[0])
    print("Check if two identical keys are equal. Should be true")
    print(Key(key.A,0,False)==Key(key.A,0,False))
    print("Check if two non-identical keys are equal. Should be false")
    print(Key(key.B,0,False)==Key(key.A,0,False))
    print("Check if two keys with different modifiers, identical symbols and modMatters=False are equal. Should be true")
    print(Key(key.A,1,False)==Key(key.A,0,False))
    print("Check if two keys with different modifiers, identical symbols and modMatters=True on one are equal. Should be false")
    print(Key(key.A,1,True)==Key(key.A,0,False))
    print("Check if two keys with different modifiers, identical symbols and modMatters=True on the other are equal. Should be false")
    print(Key(key.A,1,False)==Key(key.A,0,True))
