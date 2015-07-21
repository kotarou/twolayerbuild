import pyglet 
import entity

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

x = entity.Actor("bob")
x.respond()
y = entity.Trap("james")
y.respond()


game_window = pyglet.window.Window(800, 600) 

pyglet.app.run()