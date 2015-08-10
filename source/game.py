# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from pyglet import *
from pyglet.gl import *
from fbo import *
from ecs.exceptions import *
import numpy as np

from entity import *
from camera import *

from pyglet.window import key

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from random import randint
from color import *
from components.KeyComponent import Key
from util import *

from systems import *
from components import *

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
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.text.draw()
        self.fps.draw()

class World(object):

    def __init__(self):
        # Set up a framebuffer object
        self.fbo = FBO(800, 600)
        self.hoverItem = None
        self.hoverSwap = False
        self.lastTime = 0
        # load the example texture
        tile_file = pyglet.image.load('resources/floor_tiles.png')
        sections = []
        textures = []
        sections.append(tile_file.get_region(x=128, y=128, width=64, height=64))
        textures.append(sections[0].get_texture())
        sections.append(tile_file.get_region(x=256, y=128, width=64, height=64))
        textures.append(sections[1].get_texture())
        sections.append(tile_file.get_region(x=320, y=128, width=64, height=64))
        textures.append(sections[2].get_texture())

        # The entity manager for objects in the game
        # These components should update every tick
        self.entity_manager = EntityManager()
        self.system_manager = SystemManager(self.entity_manager)
        self.system_manager.add_system(HealthSystem())
        self.system_manager.add_system(MouseHoverSystem())

        # The manager for user inputs
        # These should only input when a user makes an action
        self.ui_manager = SystemManager(self.entity_manager)
        self.ui_manager.add_system(KeyHoldSystem())

        # The render manager. Updates to redraw graphics
        self.render_manager = SystemManager(self.entity_manager)
        self.render_manager.add_system(RenderSystem()) 
        
        # The pick manager. Updates to a seperate framebuffer than render_manager
        self.pick_manager = SystemManager(self.entity_manager)
        self.pick_manager.add_system(PickSystem())

        x = tempClass3(Color.next(), self.entity_manager)
        x.addComponent(MeshComponent(
        vertexList = [ [100, -100, 0],  
                            [100, 100, 0],   
                            [-100, 100, 0]],
        indexList  = [[0,1,2]],
        colored=True,
        colorList=Color.Red
        ))
        parseString = """
from components.HealthComponent import Health
print('hello')
for ee, health in e.eman.pairs_for_type(Health):
    if ee == e:
        health.hp = 10;
        print(health.hp)
        """
        x.addComponent(MouseClickComponent("Look at me, I'm red!"))
        #x.addComponent(MouseHoverComponent("Hovered!"))
        #x.addComponent(KeyPressComponent(Key(key.A, 0), "Hello!"))
        x.addComponent(KeyPressComponent({
            Key(key.A, 0): 'print("a")',
            Key(key.Q, key.MOD_SHIFT, True): 'print("Yo!")'
            }))
        #x.addComponent(KeyHoldComponent(Key(key.B, 0), "grrrr!"))
        x.addComponent(KeyHoldComponent({
            Key(key.W, 0): parseString,
            Key(key.S, key.MOD_SHIFT, True): 'print("sssssssssssssssssss")'
            }))
        x.addComponent(Health(10))

        y = tempClass3(Color.next(), self.entity_manager)
        y.addComponent(MeshComponent(
        Square((50,50,100), 20, Color.White, textures[2])
        ))
        y.addComponent(MouseClickComponent("Stay away!"))

        # Note that higher Z = closer to camera 


        # Can explicitly call functions on a timer
        # Only methods called from here need a dt
        # Methods called from mainLoop don't
        #clock.schedule_interval(self.update, 0.25)

    def update(self):
        time = Util.time()
        self.ui_manager.update(time-self.lastTime)
        self.system_manager.update(time-self.lastTime)
        self.hover()
        self.lastTime = time

    def draw(self):
        # Render the current frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.render_manager.update(0.5)
        
        # # Render the current picking frame
        self.fbo.attach()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity()
        self.pick_manager.update(0.5)
        self.fbo.detach()

    def hover(self):
        pass
        # if not self.hoverSwap:

        # if self.hoverItem != None:
        #     self.entity_manager.component_for_entity(self.hoverItem, MouseHoverComponent).onHover(self.hoverItem, 0, 0)


class Game(object):

    def __init__(self):
        global keys 
        keys = key.KeyStateHandler()

        self.world = World()
        self.window = window.Window(800,600, vsync=True)#fullscreen=True, vsync=True)
        
        #self.window.push_handlers(pyglet.window.event.WindowEventLogger())
        
        self.window.push_handlers(keys)

        self.camera = TopDownCamera(self.window)
        self.hud = Hud(self.window)
        clock.set_fps_limit(60)

        glEnable(GL_DEPTH_TEST)


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
    for e, mesh in game.world.entity_manager.pairs_for_type(MeshComponent):
        if e.color == Color(aa[0], aa[1], aa[2]):
            try:
                # TODO move logic into a click system
                game.world.entity_manager.component_for_entity(e, MouseClickComponent).onClick(e, x, y)
            except NonexistentComponentTypeForEntity:
                pass
    # Release the picking frame buffer
    game.world.fbo.detach()

@game.window.event                       
def on_mouse_motion(x, y, dx, dy):
    # Swap the the frame buffer where picking colors are drawn
    game.world.fbo.attach()
    # Set up storage for the pixel we click on
    aa = (GLubyte  * 3)(0)
    # Find the color of the pixel we clicked on
    pixel = gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)
    game.world.hoverItem = None
    
    # Slow, but handles mousing off something
    for e, h in game.world.entity_manager.pairs_for_type(MouseHoverComponent):
        h.active = False

    # TODO add something for caching the previously hovered item.

    # TODO construct map of color_id <=> object, find object from id. 
    #   Update such a map whenever I add a new meshcomponent.
    #   Basically, build something off ECS instead of simply using ECS at this point.

    # Find the entity with the corresponding color
    for e, mesh in game.world.entity_manager.pairs_for_type(MeshComponent):
        if e.color == Color(aa[0], aa[1], aa[2]):
            try:
                h = game.world.entity_manager.component_for_entity(e, MouseHoverComponent)
                h.active = True
                if game.world.hoverItem != e:
                    game.world.hoverSwap = True
                    game.world.hoverItem = e
                else:
                    game.world.hoverSwap = False
                break
            except NonexistentComponentTypeForEntity:
                game.world.hoverItem = None

    # Release the picking frame buffer
    game.world.fbo.detach()

@game.window.event
def on_key_press(symbol, modifiers):
    # React to the key press
    #print(modifiers)
    for e, responder in game.world.entity_manager.pairs_for_type(KeyPressComponent):
        #print(responder.actions, Key(symbol, modifiers))
        if Key(symbol, modifiers) in responder.actions.keys():
            responder.respond(Key(symbol, modifiers))
        #if responder.key == Key(symbol, modifiers):
        #        responder.respond()
    # Add the key to the holding list
    for e, holder in game.world.entity_manager.pairs_for_type(KeyHoldComponent):
        if Key(symbol, modifiers) in holder.actions.keys():
            holder.active.append(Key(symbol, modifiers))

@game.window.event
def on_key_release(symbol, modifiers):
    for e, holder in game.world.entity_manager.pairs_for_type(KeyHoldComponent):
        if Key(symbol, modifiers) in holder.actions.keys():
            holder.active.remove(Key(symbol, modifiers))
        # if holder.key == Key(symbol, modifiers):
        #         holder.active = False


game.mainLoop()


