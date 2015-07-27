# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from pyglet import *
from pyglet.gl import *
from fbo import *

import numpy as np

from entity import *
from camera import *

try:
	import Queue as Q  # ver. < 3.0
except ImportError:
	import queue as Q


GAME_TICKS_PER_SECOND 	= 60.0 
PICK_TOLERANCE 			= 3
PICK_BUFFER_SIZE 		= 256
#rendermode				= GL_RENDER	# or GL_SELECT

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
		# Set up a framebuffer object
		self.fbo = FBO(800, 600)


		a = (127, 0, 0)
		b = (0, 255, 0)
		c = (0, 0, 255)
		self.entities = [tempClass(c,c), tempClass2(b,b), tempClass3(a, a)]

		self.entityReferences = []
		# Entities go here
		# Can explicitly call functions on a timer
		# Only methods called from here need a dt
		# Methods called from mainLoop don't
		#clock.schedule_interval(self.update, 0.25)

	def update(self):
		for ent in self.entities:
			ent.update()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		#glMatrixMode(GL_MODELVIEW);
		# Run over entities and cal their draw methods
		# For now, temp:
		# glLoadIdentity()
		# glBegin(GL_LINES)
		# glColor3f(0.0, 1.0, 0.0) #// Green for x axis
		# glVertex3f(0,0,0)
		# glVertex3f(100,0,0)
		# glColor3f(1.0,0.0,0.0) #// Red for y axis
		# glVertex3f(0,0,0)
		# glVertex3f(0,100,0)
		# glColor3f(0.0,0.0,1.0) #// Blue for z axis
		# glVertex3f(0,0,0) 
		# glVertex3f(0,0,100)
		# glEnd()


		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity()
		glBegin(GL_QUADS)
		for ent in self.entities:
			ent.draw()
		glEnd()
		# ##################################
		self.fbo.attach()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW);
		# Run over entities and cal their draw methods
		# For now, temp:
		glLoadIdentity()
		glBegin(GL_QUADS)
		#glTranslatef(50,0,0)
		for ent in self.entities:
			ent.fboDraw()
		glEnd()
		self.fbo.detach()
		# ##################################




class Game(object):

	def __init__(self):
		self.world = World()
		self.window = window.Window(800,600, vsync=True)#fullscreen=True, vsync=True)
		self.camera = TopDownCamera(self.window)
		self.hud = Hud(self.window)
		clock.set_fps_limit(60)

	def mainLoop(self):
		while not self.window.has_exit:
			#print("start")
			self.window.dispatch_events()

			self.world.update()

			self.camera.worldProjection()
			self.world.draw()

			self.camera.hudProjection()
			self.hud.draw()

			clock.tick()
			self.window.flip()
			#print("end")
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
	# tex = game.world.fbo.getData()
	# for i in len(tex):
	# 	print(tex[i], tex[i+1], tex[i+2], tex[i+3])
	# 	i += 4
	#print(tex[4*(800*y+x)],tex[4*(800*y+x)+1],tex[4*(800*y+x)+2],tex[4*(800*y+x)+3])

	game.world.fbo.attach()
	pixel = [0] * 3
	aa = (GLubyte  * 3)(0)
	pixel = gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)
	for ent in game.world.entities:
		if ent.colorCompare(aa):
		 	ent.onClick(0,0)
	game.world.fbo.detach()
	print("press_ended")


game.mainLoop()


