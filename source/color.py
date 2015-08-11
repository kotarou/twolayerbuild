# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from __future__ import division

from collections import namedtuple
from random import uniform



class Color(namedtuple('__BaseColor', 'r g b')):
    """
    Colors. Add description here.
    """

    CHANNEL_MAX = 255
    uid_r       = 0
    uid_g       = 0
    uid_b       = 0


    def __new__(cls, r, g, b):
        return super(Color, cls).__new__(cls, r, g, b)

    def Random():
        return Color(
            uniform(0, Color.CHANNEL_MAX),
            uniform(0, Color.CHANNEL_MAX),
            uniform(0, Color.CHANNEL_MAX),
        )

    def invert(self):
        return Color(
            Color.CHANNEL_MAX - self.r,
            Color.CHANNEL_MAX - self.g,
            Color.CHANNEL_MAX - self.b
        )
    def darken(self):
        return Color(
            int(self.r*0.9),
            int(self.g*0.9),
            int(self.b*0.9)
        )
    def brighten(self):
        return Color(
            min(int(self.r*1.1), 255),
            min(int(self.g*1.1), 255),
            min(int(self.b*1.1), 255)
        )

    def toID(self):
        return self.r+self.g*255+self.b*255*255

    def next():
        if Color.uid_r < Color.CHANNEL_MAX:
            Color.uid_r += 1
        elif Color.uid_g < Color.CHANNEL_MAX:
            Color.uid_r = 0
            Color.uid_g += 1
        elif Color.uid_b < Color.CHANNEL_MAX:
            Color.uid_r = 0
            Color.uid_g = 0
            Color.uid_b += 1
        else:
            raise Exception()

        return Color(Color.uid_r, Color.uid_g, Color.uid_b)

    def __eq__(self, other):
        # A none color is not possible
        if other == None:
            return False
        r, g, b = self
        rr, gg, bb = other
        return r == rr and b == bb and g == gg

    def __ne__(self, other):
        return not self.__eq__(other)

Color.PureRed   = Color(255,0,0)
Color.PureGreen = Color(0,255,0)
Color.PureBlue  = Color(0,0,255)

Color.White = Color(255,255,255)
Color.Black = Color(0,0,0)

# From http://blog.xkcd.com/2010/05/03/color-survey-results/
Color.Purple = Color(126,30,156)
Color.Green = Color(21,176,26)
Color.Blue = Color(3,67,223)
Color.Pink = Color(255,129,192)
Color.Brown = Color(101,55,0)
Color.Red = Color(229,0,0)
Color.LightBlue = Color(149,208,252)
Color.Teal = Color(2,147,134)
Color.Orange = Color(249,115,6)
Color.LightGreen = Color(150,249,123)
Color.Magenta = Color(194,0,120)
Color.Yellow = Color(255,255,20)
Color.SkyBlue = Color(117,187,253)
Color.Grey = Color(146,149,145)
Color.LimeGreen = Color(137,254,5)
Color.LightPurple = Color(191,119,246)
Color.Violet = Color(154,14,234)
Color.DarkGreen = Color(3,53,0)
Color.Turquoise = Color(6,194,172)
Color.Lavender = Color(199,159,239)
Color.DarkBlue = Color(0,3,91)
Color.Tan = Color(209,178,111)
Color.Cyan = Color(0,255,255)
Color.Aqua = Color(19,234,201)
Color.ForestGreen = Color(6,71,12)
Color.Mauve = Color(174,113,129)
Color.DarkPurple = Color(53,6,62)
Color.BrightGreen = Color(1,255,7)
Color.Maroon = Color(101,0,33)
Color.Olive = Color(110,117,14)
Color.Salmon = Color(255,121,110)
Color.Beige = Color(230,218,166)
Color.Royalblue = Color(5,4,170)
Color.NavyBlue = Color(0,17,70)
Color.lilac = Color(206,162,253)
Color.HotPink = Color(255,2,141)
Color.Lightbrown = Color(173,129,80)
Color.PaleGreen = Color(199,253,181)
Color.Peach = Color(255,176,124)
Color.OliveGreen = Color(103,122,4)
Color.DarkPink = Color(203,65,107)
Color.Periwinkle = Color(142,130,254)
Color.SeaGreen = Color(82,252,161)
Color.Lime = Color(170,255,50)
Color.Indigo = Color(56,2,130)
Color.Mustard = Color(206,179,1)
Color.LightPink = Color(255,209,223)






