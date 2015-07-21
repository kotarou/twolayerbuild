import pyglet 
import entity

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

x = entity.Actor("bob")
x.respond()
y = entity.Trap("james")
y.respond()


game_window = pyglet.window.Window(800, 600) 



@game_window.event
def on_draw(): 
    print("hi")
    game_window.clear() 
    x.draw()    
    #level_label.draw() 
    #score_label.draw()
    
    
pyglet.app.run()