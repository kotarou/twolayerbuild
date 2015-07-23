from pyglet.gl import *

class Camera(object):
    """ 
        Generic camera class
    """
    def __init__(self, viewport=(-400, 400, -300, 300), pos=(0,0,-10), lookAt=(0,0,0), up=(0,1,0)):
        # Projection for the HUD
        self.left   = viewport[0]
        self.right  = viewport[1]
        self.bottom = viewport[2]
        self.top    = viewport[3]
        self.close  = viewport[4] 
        self.far    = viewport[5]
        
        self.xPos   = pos[0] 
        self.yPos   = pos[1]
        self.zPos   = pos[2]

        # Not currently used
        # self.xZoom  = zoom[0]
        # self.yZoom  = zoom[1]
        # self.zZoom  = zoom[2]

        self.xLook = lookAt[0]
        self.yLook = lookAt[1]
        self.zLook = lookAt[2]

        self.xUp   = up[0]
        self.yUp   = up[1]
        self.zUp   = up[2]

    def worldProjection(self):
        """
            Look at worldspace.
            By default this is the area bounded by [-400, 400], [-300, 300], [-255,255] around (0,0,0)
            This means (0,0,0) is the center of the screen-space
        """

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # Make yMax be at the top of the screen
        glScalef(1.0, -1.0, 1.0)
        # Specify the camera bounds
        glOrtho(self.left, self.right, self.top, self.bottom, self.close, self.far)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Place the camera and rotate it
        # (eyeX, eyeY, eyeZ, lookAtX, lookAtY, lookAtZ, xUp, yUp, zUp)
        gluLookAt(self.xPos, self.yPos, self.zPos, self.xLook, self.yLook, self.zLook, self.xUp, self.yUp, self.zUp)
        
    def hudProjection(self):
        """ 
            Look at screenspace.
            (0,0) is the bottom left corner of the screen
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #Reset the view matrix that so we are rendering in screen-space
        gluOrtho2D(0, 2*self.right, 0, 2*self.top)

class TopDownCamera(Camera):
    """ 
        Simple camera with a top down viewport
    """

    def __init__(self, window):
        Camera.__init__(self, viewport=(-window.width / 2.0, window.width / 2.0, -window.height / 2.0, window.height / 2.0, -255, 255))



