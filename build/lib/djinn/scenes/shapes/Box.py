import pygame
from pygame.locals import *
from image import *
from OpenGL.GL import *
from OpenGL.GLU import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
from djinn.scenes.textures.Texture import *

class Box:
	def __init__(self,length,breadth,height,x,y,z,color,fname):
		self.length = length    
		self.breadth = breadth
		self.height = height
		self._x = x
		self._y = y
		self._z = z
		self.color = color
		self.fname = fname
	def build(self):
                glPushMatrix()
		material = Material()
		material.init(128)
                glShadeModel(GL_SMOOTH)
		tex = Texture(self.fname)
		glBindTexture(GL_TEXTURE_2D,tex.loadTexture())
		glBegin(GL_QUADS)
        	glTexCoord2f(0.0, 2.0); glVertex3f(-1.0 + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
    		glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x, -1.0 + self._y,  1.0*self.length + self._z);
      		glTexCoord2f(2.0, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(2.0, 2.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(2.0, 0.0); glVertex3f(-1.0 + self._x, -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(2.0, 2.0); glVertex3f(-1.0 + self._x,  1.0*self.height + self._y , -1.0 + self._z);
        	glTexCoord2f(0.0, 2.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth +self._x, -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 4.0); glVertex3f(-1.0 + self._x ,  1.0*self.height+self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x ,  1.0*self.height+ self._y,  1.0*self.length + self._z);
        	glTexCoord2f(4.0, 0.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
       		glTexCoord2f(4.0, 4.0); glVertex3f( 1.0*self.breadth + self._x ,  1.0*self.height + self._y, -1.0 + self._z);
        	glTexCoord2f(4.0, 4.0); glVertex3f(-1.0 + self._x , -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 4.0); glVertex3f( 1.0 *self.breadth + self._x, -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(4.0, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(4.0, 0.0); glVertex3f( 1.0*self.breadth + self._x, -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(4.0, 4.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y, -1.0 + self._z);
        	glTexCoord2f(0.0, 4.0); glVertex3f( 1.0*self.breadth + self._x,  1.0*self.height + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0*self.breadth + self._x , -1.0 + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y, -1.0 + self._z);
        	glTexCoord2f(4.0, 0.0); glVertex3f(-1.0 + self._x , -1.0 + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(4.0, 4.0); glVertex3f(-1.0 + self._x ,  1.0*self.height + self._y,  1.0*self.length + self._z);
        	glTexCoord2f(0.0, 4.0); glVertex3f(-1.0 + self._x ,  1.0*self.height+ self._y, -1.0 + self._z);	
		glEnd()
		glDeleteTextures(1)
                glPopMatrix()
