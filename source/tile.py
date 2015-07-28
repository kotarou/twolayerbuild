from abc import ABCMeta, abstractmethod
import pyglet


class Tile:

	__metacass__ = ABCMeta

	name = ""
	description = ""
	identifier = ""

	navigatable = ""
	draw = ""
	owner = ""

	pos = ([0.0, 0.0])
	
	def __init__(self, identifier, owner, inX, inY):
		self.identifier = identifier
		self.pos[0] = inX
		self.pos[1] = inY
		self.owner = owner

	@abstractmethod
	def draw(self): pass

	# TODO: is called when an entity moves onto this tile?
	#	When some other things calls its trigger?
	@abstractmethod
	def trigger(self): pass