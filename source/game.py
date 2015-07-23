# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from pyglet import *
from pyglet.gl import *

import numpy as np

from entity import *
from camera import *

try:
	import Queue as Q  # ver. < 3.0
except ImportError:
	import queue as Q


GAME_TICKS_PER_SECOND 	= 60.0 

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

class Hud(object):

	def __init__(self, win):
		helv = font.load('Helvetica', win.width / 30.0)
		self.text = font.Text(
			helv,
			'Two Layer Game',
			x=10,
			y=win.height - 10,
			halign=font.Text.LEFT,
			valign=font.Text.TOP,
			color=(1, 1, 1, 0.5),
		)
		self.fps = clock.ClockDisplay()

	def draw(self):
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity();
		self.text.draw()
		self.fps.draw()

class World(object):

	def __init__(self):
		print("setup")
		self.entities = []
		# Entities go here
		# Can explicitly call functions on a timer
		# Only methods called from here need a dt
		# Methods called from mainLoop don't
		#clock.schedule_interval(self.update, 0.25)

	def update(self):
		for ent in self.entities:
			ent.update()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity();
		# Run over entities and cal their draw methods
		# For now, temp:
		glLoadIdentity()
		glBegin(GL_LINES)
		glColor3f(0.0, 1.0, 0.0) #// Green for x axis
		glVertex3f(0,0,0)
		glVertex3f(100,0,0)
		glColor3f(1.0,0.0,0.0) #// Red for y axis
		glVertex3f(0,0,0)
		glVertex3f(0,100,0)
		glColor3f(0.0,0.0,1.0) #// Blue for z axis
		glVertex3f(0,0,0) 
		glVertex3f(0,0,100)
		glEnd()


		glBegin(GL_QUADS)
		#glTranslatef(50,0,0)
		glColor3f(1.0, 0.0, 0.0)
		glVertex3f(-10	, -10	, 0)
		glVertex3f(-10	, 10	, 0)
		glVertex3f(10	, 10	, 0)
		glVertex3f(10	, -10	, 0.0)
		glEnd()


		for ent in self.entities:
			ent.draw()



class Game(object):

	def __init__(self):
		self.world = World()
		self.window = window.Window(800,600, vsync=True)#fullscreen=True, vsync=True)
		self.camera = TopDownCamera(self.window)
		self.hud = Hud(self.window)
		clock.set_fps_limit(60)

	def mainLoop(self):
		while not self.window.has_exit:
			self.window.dispatch_events()

			self.world.update()

			self.camera.worldProjection()
			self.world.draw()

			self.camera.hudProjection()
			self.hud.draw()

			clock.tick()
			self.window.flip()
game = Game()



def glFindObjectUnderCursor(x, y):
	pass

@game.window.event
def on_mouse_press(x, y, button, modifiers):
	"""
		Event that fires whenever a mouse button is clicked.
		x, y 		:	(int)	The coordinates of the mouse click location
		button		:	(int)	The mouse button that was pressed. 1 = left click, 4 = right click
		modifiers	:	(int)	Modifying keys that were pressed in conjunction with the mouse
	"""
	print("Mouse clicked")
	a = glFindObjectUnderCursor(x, y)
	if type(a) != type(None):
		print("You clicked on ", a.handle)
		#a.respond()
		#print("you clicked on", a.toString())




# def findObjectUnderCursor(x, y):
# 	""" 
# 		Find the object under the cursor.
# 		Return interface components (menus/etc) before game objects.
# 		Not there is currently no z-buffer, so it does not check for which object is ontop yet.
# 	"""
# 	for ent in interface:
# 		ob = RfindObjectUndercursor(ent, x, y)
# 		if ob != None:
# 			return ob
# 	for ent in renderables:
# 		ob = RfindObjectUndercursor(ent, x, y)
# 		if ob != None:
# 			return ob
# 	return None


# def RfindObjectUndercursor(ent, x, y):
# 	"""
# 		Recursive portion of finding objects under cursor
# 		Checks through an entities children to check if they intersct as well.
# 	"""
# 	if len(ent.children) > 0:
# 		for child in ent.children:
# 			ob = RfindObjectUndercursor(child, x, y)
# 			if ob != None:
# 				return ob
# 	if ent.intersect(x,y):

# 		return ent
# 	else:
# 		return None



game.mainLoop()





# @game_window.event
# def on_key_press(symbol, modifiers):
# 	"""
# 		Event that fires whenever a key is pressed.
# 		symbol		:	(int) The key that was pressed. Use key.A / key.LEFT / etc for comparison
# 							See pyglet.window.key for a list of keys
# 		modifiers	:	(int) Modifying keys that were pressed
# 	"""
# 	print(symbol, ' was pressed')

