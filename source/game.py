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


from color import *
from util import *

GAME_TICKS_PER_SECOND 	= 60.0 
PICK_TOLERANCE 			= 3
PICK_BUFFER_SIZE 		= 256
# VERTEX_SHADER = shaders.compileShader(
# 	"""
# 	#version 120 
# 	void main() { 
# 		gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex; 
# 	}
# 	""", GL_VERTEX_SHADER)

# FRAGMENT_SHADER = shaders.compileShader(
# 	"""
# 	#version 120 
# 	void main() { 
# 		gl_FragColor = vec4( 0, 1, 0, 1 ); 
# 	}
# 	""", GL_FRAGMENT_SHADER)

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
		# Note that higher Z = closer to camera 
		self.entities = [tempClass(Color.next(),Square((100,100,100), 10, Color.Blue)),
						 tempClass(Color.next(),Triangle((100,150,100), 20, Color.Red)), 
						 tempClass(Color.next(),Color.Green,[[-70, -70, 100],  [-70, +70, 100],   [+70, 70, 100]],[[0,1,2]]),
						 tempClass(Color.next(),Color.Yellow,[[-20, -20, 150],  [-20, +20, 150],   [+20, 20, 150], [20, -20, 150]],[[0,1,2], [2,3,0]])]
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
		# Render the current frame
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity()
		for ent in self.entities:
			ent.draw()
		
		# Render the current picking frame
		self.fbo.attach()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity()
		for ent in self.entities:
			ent.fboDraw()
		self.fbo.detach()



class Game(object):

	def __init__(self):
		self.world = World()
		self.window = window.Window(800,600, vsync=True)#fullscreen=True, vsync=True)
		self.camera = TopDownCamera(self.window)
		self.hud = Hud(self.window)
		clock.set_fps_limit(60)

		glEnable(GL_DEPTH_TEST)


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

	# Swap the the frame buffer where picking colors are drawn
	game.world.fbo.attach()
	# Set up storage for the pixel we click on
	aa = (GLubyte  * 3)(0)
	# Find the color of the pixel we clicked on
	pixel = gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)
	print(aa[0], aa[1], aa[2])
	# Find the entity with the corresponding color
	for ent in game.world.entities:
		if ent.handle == Color(aa[0], aa[1], aa[2]):
		 	ent.onClick(0,0)
	# Release the picking frame buffer
	game.world.fbo.detach()



game.mainLoop()


