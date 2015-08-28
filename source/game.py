# -*- coding: utf-8 -*-
"""
@author: Kotarou
"""
from pyglet import *
from pyglet.gl import *
from fbo import *
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

from entities import *

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
        # Component systems update first. These control game logic
        self.system_manager.addSystem("component", HealthSystem())
        self.system_manager.addSystem("component", SVASystem())
        self.system_manager.addSystem("component", CollisionSystem())

        # Interaction systems handle to user input. These update after the game logic has processed
        self.system_manager.addSystem("interaction", MouseHoverSystem())
        self.system_manager.addSystem("interaction", KeyHoldSystem())

        # Render systems handle anything that draws to the main game window
        self.system_manager.addSystem("render", RenderSystem())

        # Pick systems also involve rendering, but to the color picking FBO instead.
        self.system_manager.addSystem("pick", PickSystem())

        # x = Entity(self.entity_manager)
        # x.addComponent(MeshComponent(shape=Square(50, Vector(0, 0, 0), CENTER, [Color(255,0,255)*4], None)))
        # x.addComponent(SVAComponent(Vector(0,0,0),a_velocity=Vector(0,0,0)))
        # x.addComponent(CollisionComponent(useAABB=True, type_="thing", typeCollide=["thing","ground"]))

        # y = Entity(self.entity_manager)
        # y.addComponent(MeshComponent(shape=Square(50, Vector(100, 0, 0), TOPLEFT, colorList=None, texture=textures[2])))
        # y.addComponent(SVAComponent(Vector(100,0,0)))
        # y.addComponent(CollisionComponent(useAABB=True, type_="thing", typeCollide=["thing","ground"]))

        # listOfThings = []
        # for i in range (0, 16):
        #     a = Entity(self.entity_manager)
        #     a.addComponent(MeshComponent(shape=Square(50, Vector(0,0,0), TOPLEFT, colorList=[Color(255,255,255)*4])))
        #     a.addComponent(SVAComponent(Vector(-400+(50*i), -100, 0)))
        #     a.addComponent(CollisionComponent(useAABB=False, type_="ground", typeCollide=["thing"]))
        #     listOfThings.append(a)

        ground = Entity(self.entity_manager)
        ground.addComponent(MeshComponent(shape=Rectangle(800, 50, Vector(0,0,0), TOPLEFT, colorList=[Color(255,255,0)*4])))
        ground.addComponent(SVAComponent(Vector(-400, -200, 0)))
        ground.addComponent(CollisionComponent(useAABB=True, type_="ground", typeCollide=["limb"]))

        p1Avatar = Actor(self.entity_manager)
        p1Avatar.addSVAComponent(position=Vector(-350, -190, 0), bounded=True)
        p2Avatar = Actor(self.entity_manager)
        p2Avatar.addSVAComponent(position=Vector(350, -190, 0), bounded=True)

# #         x.addComponent(MouseClickComponent("Look at me, I'm red!"))
#         x.addComponent(MouseHoverComponent("""
# from random import uniform
# owner.getSingleComponentByType(SVAComponent).S += Vector(uniform(-100,100),uniform(-100,100),0)
#                        """, "Hovered!"))
# #         #x.addComponent(KeyPressComponent(Key(key.A, 0), "Hello!"))
# #         x.addComponent(KeyPressComponent({
# #             Key(key.A, 0): 'print("asdf")',
# #             Key(key.Q, key.MOD_SHIFT, True): 'print("Yo!")'
# #             }))
# #         #x.addComponent(KeyHoldComponent(Key(key.B, 0), "grrrr!"))
# #         x.addComponent(Health(10))



# # #         y.addComponent(MouseClickComponent("Stay away!"))

#         y.addComponent(KeyHoldComponent({Key(key.W, 0): ["""
# owner.getSingleComponentByType(SVAComponent).S += Vector(0,1,0)
# """]}))
# # #         y.addComponent(KeyHoldComponent({Key(key.Q, 0): [
# # # """
# # # owner.getSingleComponentByType(SVAComponent).V = Vector(0,1,0)
# # # """,
# # # """
# # # owner.getSingleComponentByType(SVAComponent).V = Vector(0,0,0)
# # # """
# # # ]}))
#         y.addComponent(KeyHoldComponent({Key(key.S, 0): ["""
# owner.getSingleComponentByType(SVAComponent).S += Vector(0,-1,0)
# """]}))
#         y.addComponent(KeyHoldComponent({Key(key.A, 0): ["""
# owner.getSingleComponentByType(SVAComponent).S += Vector(-1,0,0)
# """]}))
#         y.addComponent(KeyHoldComponent({Key(key.D, 0): ["""
# owner.getSingleComponentByType(SVAComponent).S += Vector(1,0,0)
# """]}))
# #         # Note that higher Z = closer to camera


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
            #print("Hovering over object at", x, y)
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
        glLoadIdentity()
        # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        #     [0, 1, 2, 0, 2, 3],
        #     ('v3f', (100, 100, 0,
        #              150, 100, 0,
        #              150, 150, 0,
        #              100, 150, 0)),
        #     ('c3B', (0, 0, 255, 0, 255, 0, 255, 0, 0, 128, 128, 128))
        # )
        # vertex_list = pyglet.graphics.vertex_list(2,
        #         ('v3i', (0, 0, 0, 20,100,0)),
        #         ('c3B', (255,255,255, 255,0,0))
        # )
        # vertex_list.draw(pyglet.gl.GL_LINES)
        v2 = pyglet.graphics.vertex_list(6,
                ('v3i', (0, 0, 0, 100,0,0, 0, 0, 0, 0,100,0, 0,0,0, 0,0,100)),
                ('c3B', (255,255,255, 255,0,0, 255,255,255, 0,255,0, 255,255,255, 0,0,255))
        )
        v2.draw(pyglet.gl.GL_LINES)
        # Render the current picking frame
        # This frame is rendered in screen-space (0,0)->(game.window.width,game.window.height)
        self.fbo.attach()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        self.system_manager.update("pick",cTime-self.lastTime)
        self.fbo.detach()

class Game(object):

    def __init__(self):
        global keys
        keys = key.KeyStateHandler()

        self.world = World()
        self.window = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT, vsync=True)  # fullscreen=True, vsync=True)

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

def cidFromMouse(x, y):
    # Swap the the frame buffer where picking colors are drawn
    game.world.fbo.attach()
    # Set up storage for the pixel we click on
    aa = (GLubyte  * 3)(0)
    # Find the color of the pixel we clicked on
    gl.glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, aa)

    # Release the picking frame buffer
    game.world.fbo.detach()
    # Generate the id of the color we cllicked on
    return Color(aa[0], aa[1], aa[2]).toID()

@game.window.event
def on_mouse_press(x, y, button, modifiers):
    """
        Event that fires whenever a mouse button is clicked.
        x, y 		:	(int)	The coordinates of the mouse click location
        button		:	(int)	The mouse button that was pressed. 1 = left click, 4 = right click
        modifiers	:	(int)	Modifying keys that were pressed in conjunction with the mouse
    """
    cid = cidFromMouse(x, y)

    # Search for the mesh with id in the database of color ids
    # If we find it, run the on Click event for each MouseClickComponent attached to the owner of the mesh we clicked on
    try:
        mesh = game.world.entity_manager.cidDatabase[cid]
        for clickable in game.world.entity_manager.componentByType(mesh.owner, MouseClickComponent):
            clickable.onClick(mesh.owner, x, y)
    except KeyError:
        pass

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
