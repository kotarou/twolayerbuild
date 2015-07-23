from abc import ABCMeta, abstractmethod
import pyglet


class Tile:

	__metacass__ = ABCMeta

	name = ""
	description = ""
	identifier = ""

	navigatable = ""

	pos = np.array([0.0, 0.0])
	
	def __init__(self, identifier):
		self.identifier = identifier

	@abstractmethod
	def draw(self): pass

class Floor(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	navigatable = True

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		pos[0] = inX
		pos[1] = inY

class Wall(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	navigatable = False

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		pos[0] = inX
		pos[1] = inY

class Corridor(Tile):

	sprite = ""

	name = ""
	description = ""
	identifier = ""

	navigatable = True

	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		pos[0] = inX
		pos[1] = inY