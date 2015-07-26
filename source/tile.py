from abc import ABCMeta, abstractmethod
import pyglet


class Tile:

	__metacass__ = ABCMeta

	name = ""
	description = ""
	identifier = ""

	navigatable = ""

	pos = ([0.0, 0.0])
	
	def __init__(self, identifier, inX, inY):
		self.identifier = identifier
		pos[0] = inX
		pos[1] = inY

	@abstractmethod
	def draw(self): pass

	# TODO: is called when an entity moves onto this tile?
	@abstractmethod
	def trigger(self): pass