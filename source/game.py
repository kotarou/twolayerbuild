import pyglet 
import entity

GAME_TICKS_PER_SECOND 	= 60.0 

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

xx = entity.Actor(identifier="bob",x=100,y=100)
xx.respond()
y = entity.Trap("james")
y.respond()


game_window = pyglet.window.Window(800, 600) 

renderables =[xx]
interface = [y]

@game_window.event
def on_draw(): 
	# Clear the game window to a black background
	game_window.clear() 

	# Render all objects that need rendering
	for ent in renderables:
		ent.draw()
    
	# Render the interface
	for ent in interface:
		ent.draw()

	# Console debugging
	# print("Window redrawn")
    
    #level_label.draw() 
    #score_label.draw()

def update(dt): 
	for ent in renderables: 
		ent.update(dt)
  

@game_window.event
def on_mouse_press(x, y, button, modifiers):
	print("Mouse clicked")
	xx.setPosition(x,y)

@game_window.event
def on_key_press(symbol, modifiers):
    print(symbol, ' was pressed')

pyglet.clock.schedule_interval(update, 1/GAME_TICKS_PER_SECOND) 
pyglet.app.run()