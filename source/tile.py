from abc import ABCMeta, abstractmethod
import pyglet


class Tile:

	__metacass__ = ABCMeta

	name = ""
	description = ""
	identifier = ""

	navigatable = ""
	
	def __init__(self, identifier):
		self.identifier = identifier

	@abstractmethod
	def draw(self): pass

class Floor(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	posX = 0
	posY = 0

	navigatable = True

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		self.posX = inX
		self.posY = inY

class Wall(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	posX = 0
	posY = 0

	navigatable = False

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		self.posX = inX
		self.posY = inY

class Corridor(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	posX = 0
	posY = 0

	navigatable = True

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		self.posX = inX
		self.posY = inY