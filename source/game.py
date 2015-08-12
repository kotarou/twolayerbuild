# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from pyglet import *
from pyglet.gl import *
from fbo import *
from ecs.exceptions import *
import numpy as np

from managers import *

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
import time
GAME_TICKS_PER_SECOND 	= 60.0
PICK_TOLERANCE 			= 3
PICK_BUFFER_SIZE 		= 256
WINDOW_WIDTH            = 800   # soft variable game.window.width
WINDOW_HEIGHT           = 600   # soft variable game.window.height
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

def currTime():
    return int(round(time.time() * 1000))

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
        self.mousePosition = (0,0)
        self.mouseMovement = (0,0)
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
        self.system_manager.addSystem("component", HealthSystem())
        self.system_manager.addSystem("component", SVASystem())
        self.system_manager.addSystem("interaction", MouseHoverSystem())

        self.system_manager.addSystem("interaction", KeyHoldSystem())

        self.system_manager.addSystem("render", RenderSystem())
        self.system_manager.addSystem("pick", PickSystem())

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
print("hi!!!")
        """
        x.addComponent(SVAComponent(Vector(-100,-100,0),a_velocity=Vector(0,0,1)))
        x.addComponent(MouseClickComponent("Look at me, I'm red!"))
        x.addComponent(MouseHoverComponent("Hovered!"))
        #x.addComponent(KeyPressComponent(Key(key.A, 0), "Hello!"))
        x.addComponent(KeyPressComponent({
            Key(key.A, 0): 'print("asdf")',
            Key(key.Q, key.MOD_SHIFT, True): 'print("Yo!")'
            }))
        #x.addComponent(KeyHoldComponent(Key(key.B, 0), "grrrr!"))
        x.addComponent(Health(10))

        y = tempClass3(Color.next(), self.entity_manager)
        y.addComponent(SVAComponent(Vector(-100,-100,0)))
        y.addComponent(MeshComponent(
        Square((50,50,100), 20, Color.White, textures[2])
        ))
        y.addComponent(MouseClickComponent("Stay away!"))

        y.addComponent(KeyHoldComponent({Key(key.W, 0): ["""
from util import Vector
from components import *
owner.eman.componentByType(owner, SVAComponent)[0].V = Vector(1,0,0)

""", """
from util import Vector
from components import *
owner.eman.componentByType(owner, SVAComponent)[0].V = Vector(0,0,0)

"""]}))
        # Note that higher Z = closer to camera


        # Can explicitly call functions on a timer
        # Only methods called from here need a dt
        # Methods called from mainLoop don't
        #clock.schedule_interval(self.update, 0.25)

    def mouseHandle(self, x, y, dx, dy):
         # Swap the the frame buffer where picking colors are drawn
        game.world.fbo.attach()
        # Set up storage for the pixel we click on
        aa = (GLubyte  * 3)(0)
        # Find the color of the pixel we clicked on
        pixel = gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)
        cid = Color(aa[0], aa[1], aa[2]).toID()

        try:
            mesh = game.world.entity_manager.cidDatabase[cid]
            # If a different object was hovered on, set its hover state to false
            if game.world.hoverItem != mesh.owner and game.world.hoverItem is not None:
                for hoverable in game.world.entity_manager.componentByType(game.world.hoverItem, MouseHoverComponent):
                    hoverable.active = False
            # Set the hover state of the current object to True
            for hoverable in game.world.entity_manager.componentByType(mesh.owner, MouseHoverComponent):
                hoverable.active = True
            print("Hovering over object at", x, y)
            game.world.hoverItem = mesh.owner
        except KeyError:
            # We are hovering over nothing.
            if game.world.hoverItem is not None:
                for hoverable in game.world.entity_manager.componentByType(game.world.hoverItem, MouseHoverComponent):
                    hoverable.active = False
            game.world.hoverItem = None

        # Release the picking frame buffer
        game.world.fbo.detach()

    def update(self):
        cTime = currTime()
        #self.ui_manager.update(time-self.lastTime)
        self.system_manager.update("component",cTime-self.lastTime)
        self.system_manager.update("interaction",cTime-self.lastTime)

        # If the mouse has not moved, we still need to update hover code
        # TODO: Add check for mouse having not moved
        self.mouseHandle(self.mousePosition[0], self.mousePosition[1],
                         self.mouseMovement[0], self.mouseMovement[1])
        self.mouseMovement = (0,0)
        self.lastTime = cTime

    def draw(self):
        cTime = currTime()
        # Render the current frame
        # This frame is rendered in world-space (-game.window.width / 2,-game.window.height / 2)
        #                                     ->(game.window.width / 2,game.window.height / 2)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        self.system_manager.update("render",cTime-self.lastTime)

        # Render the current picking frame
        # This frame is rendered in screen-space (0,0)->(game.window.width,game.window.height)
        self.fbo.attach()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW);
        self.system_manager.update("pick",cTime-self.lastTime)
        self.fbo.detach()

class Game(object):

    def __init__(self):
        global keys
        keys = key.KeyStateHandler()

        self.world = World()
        self.window = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT, vsync=True)#fullscreen=True, vsync=True)

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

    # Swap the the frame buffer where picking colors are drawn
    game.world.fbo.attach()
    # Set up storage for the pixel we click on
    aa = (GLubyte  * 3)(0)
    # Find the color of the pixel we clicked on
    pixel = gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)

    # Generate the id of the color we cllicked on
    cid = Color(aa[0], aa[1], aa[2]).toID()

    # Search for the mesh with id in the database of color ids
    # If we find it, run the on Click event for each MouseClickComponent attached to the owner of the mesh we clicked on
    try:
        mesh = game.world.entity_manager.cidDatabase[cid]
        for clickable in game.world.entity_manager.componentByType(mesh.owner, MouseClickComponent):
            clickable.onClick(mesh.owner, x, y)
    except KeyError:
        pass

    # Release the picking frame buffer
    game.world.fbo.detach()

@game.window.event
def on_mouse_motion(x, y, dx, dy):
    """
        Event that fires whenever the mouse moves
        x, y        :   (int)   The coordinates of the mouse location in screen-space
        dx, dy      :   (int)   The change in mouse position
    """
    game.world.mousePosition = (x, y)
    game.world.mouseMovement = (dx, dy)


@game.window.event
def on_key_press(symbol, modifiers):
    """
        Event that fires whenever a key is pressed.
        symbol      :   (key)   The key that was pressed
        modifiers   :   (int)   Modifying keys that were pressed in conjunction.
                                To test if a modifier was pressed, use modifiers & key.MOD_SHIFT > 0
    """
    # Set up a "dummy" key to check against
    k = Key(symbol, modifiers)
    # React to the key press
    for e, responder in game.world.entity_manager.pairsForType(KeyPressComponent):
        if k in responder.actions.keys():
            responder.respond(k)

    # Add the key to the holding list
    for e, holder in game.world.entity_manager.pairsForType(KeyHoldComponent):
        if k in holder.actions.keys():
            holder.active.append(Key(symbol, modifiers))

@game.window.event
def on_key_release(symbol, modifiers):
    """
        Event that fires whenever a key is released.
        symbol      :   (key)   The key that was released
        modifiers   :   (int)   Modifying keys that were pressed in conjunction.
                                To test if a modifier was pressed, use modifiers & key.MOD_SHIFT > 0
    """
    for e, holder in game.world.entity_manager.pairsForType(KeyHoldComponent):
        if Key(symbol, modifiers) in holder.actions.keys():
            holder.active.remove(Key(symbol, modifiers))



game.mainLoop()


