from __future__ import division

from collections import namedtuple
from random import uniform



class Color(namedtuple('__BaseColor', 'r g b')):
    """
    Colors look at here for some names to use: http://blog.xkcd.com/2010/05/03/color-survey-results/
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

Color.Red   = Color(255,0,0)
Color.White = Color(255,255,255)

