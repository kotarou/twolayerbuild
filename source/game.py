import pyglet 
import entity

GAME_TICKS_PER_SECOND 	= 60.0 

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

xx = entity.Actor(identifier="bob",x=100,y=100)
xx.respond()
xx.setVelocity(1,1)
y = entity.Trap("james")
y.respond()


game_window = pyglet.window.Window(800, 600) 

renderables =[xx]
interface = [y]

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
	xx.setPosition(x,y)
	print(xx.renderable)

@game_window.event
def on_key_press(symbol, modifiers):
	"""
		Event that fires whenever a key is pressed.
		symbol		:	(int) The key that was pressed. Use key.A / key.LEFT / etc for comparison
							See pyglet.window.key for a list of keys
		modifiers	:	(int) Modifying keys that were pressed
	"""
	print(symbol, ' was pressed')

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