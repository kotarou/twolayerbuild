import pyglet 
import entity

GAME_TICKS_PER_SECOND 	= 60.0 

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

xx = entity.Actor(identifier="bob",x=100,y=100, sx=50, sy=50, vx=3.0, vy=3.0, color=(1.0,0,0))
yy = entity.Actor(identifier="james",x=10,y=10, sx=30, sy=30, parent=xx, color=(0,1.0,0))
zz = entity.Actor(identifier="andrew",x=10,y=10, sx=10, sy=10, parent=yy, color=(0,0,1.0))
yy.addChild(zz)
xx.addChild(yy)

print(yy.toString())

game_window = pyglet.window.Window(800, 600) 

# Going to need to work out how to add children into this
renderables =[xx]
interface = []

@game_window.event
def on_draw(): 
	"""
		Main game draw method: redraw the game window whenever called.
	"""
	# Clear the game window to a black background
	game_window.clear() 

	# Render all objects that need rendering
	for ent in renderables:
		ent.draw()
	
	# Render menus

	# Render interface
	draw_fps()

	# Console debugging
	# print("Window redrawn")
	
	#level_label.draw() 
	#score_label.draw()

def update(dt): 
	""" 
		Game update method. Is called every tick 
		dt			:	(float)	Time since previous update call
	"""
	for ent in renderables: 
		ent.update(dt)
  

@game_window.event
def on_mouse_press(x, y, button, modifiers):
	"""
		Event that fires whenever a mouse button is clicked.
		x, y 		:	(int)	The coordinates of the mouse click location
		button		:	(int)	The mouse button that was pressed. 1 = left click, 4 = right click
		modifiers	:	(int)	Modifying keys that were pressed in conjunction with the mouse
	"""
	print("Mouse clicked")
	a = findObjectUnderCursor(x, y)
	if type(a) != type(None):
		a.respond()
		print("you clicked on", a.toString())


@game_window.event
def on_key_press(symbol, modifiers):
	"""
		Event that fires whenever a key is pressed.
		symbol		:	(int) The key that was pressed. Use key.A / key.LEFT / etc for comparison
							See pyglet.window.key for a list of keys
		modifiers	:	(int) Modifying keys that were pressed
	"""
	print(symbol, ' was pressed')

def findObjectUnderCursor(x, y):
	""" 
		Find the object under the cursor.
		Return interface components (menus/etc) before game objects.
		Not there is currently no z-buffer, so it does not check for which object is ontop yet.
	"""
	for ent in interface:
		ob = RfindObjectUndercursor(ent, x, y)
		if ob != None:
			return ob
	for ent in renderables:
		ob = RfindObjectUndercursor(ent, x, y)
		if ob != None:
			return ob
	return None

def RfindObjectUndercursor(ent, x, y):
	"""
		Recursive portion of finding objects under cursor
		Checks through an entities children to check if they intersct as well.
	"""
	if len(ent.children) > 0:
		for child in ent.children:
			ob = RfindObjectUndercursor(child, x, y)
			if ob != None:
				return ob
	if ent.intersect(x,y):

		return ent
	else:
		return None


def draw_fps():
	""" 
		Draw the fps counter in the bottom right of the screen.
	"""
		
	label = pyglet.text.Label("fps: %4.2f" % pyglet.clock.get_fps(),
						font_name='Times New Roman',
						font_size=24,
						x=game_window.width-100, y=70,
						anchor_x='center', anchor_y='center')
	label.draw()

pyglet.clock.schedule_interval(update, 1/GAME_TICKS_PER_SECOND) 
pyglet.app.run()