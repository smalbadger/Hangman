'''
Class:      HangmanDrawingBox
Author(s):  Clarissa Badger
Date:       Dec 23, 2018
Type:       FINAL
Description:
            view to draw the hangman
'''

from PySide2.QtWidgets import *
from PySide2.QtCore import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PySide2.QtOpenGL import *

import numpy as np

class HangmanDrawingBox(QGLWidget):

    lose = Signal()

    def __init__(self):
        super().__init__()
        self.wrongGuesses = 0
        self.rightGuesses = 0
        
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        self.drawHangyThing()
        
        if self.wrongGuesses >= 1:
            self.drawHead()
            
        if self.wrongGuesses >= 2:
            self.drawTorso()
            
        if self.wrongGuesses >= 3:
            self.drawArms()
            
        if self.wrongGuesses >= 4:
            self.drawLegs()
            
    def drawHangyThing(self):
        glColor(0.0,0.0,0.0,1.0)
        glLineWidth(5.0)
        glBegin(GL_LINE_STRIP)
        glVertex2f( 0,  6)
        glVertex2f( 0,  7)
        glVertex2f( 5,  7)
        glVertex2f( 5, -7)
        glVertex2f(-2, -7)
        glVertex2f( 9, -7)
        glEnd()
        
    def drawHead(self):
        print("drawing head")
        glPushMatrix()
        glTranslatef(0, 5, 0)
        
        glBegin(GL_LINE_LOOP)
        for i in range(100):
            theta = 2 * np.pi * i / 100
            x = np.cos(theta)
            y = np.sin(theta)
            glVertex2f(x, y)
        glEnd()
        
        glPopMatrix()
        
    def drawTorso(self):
        glBegin(GL_LINES)
        glVertex2f(0, 4)
        glVertex2f(0, 0)
        glEnd()
        
    def drawArms(self):
        glBegin(GL_LINES)
        glVertex2f(0, 3)
        glVertex2f(2, 2)
        glVertex2f(0, 3)
        glVertex2f(-2, 2)
        glEnd()
        
    def drawLegs(self):
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(2, -2)
        glVertex2f(0, 0)
        glVertex2f(-2, -2)
        glEnd()
        
    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-10,10,-10,10)
        glMatrixMode(GL_MODELVIEW)
        
    def initializeGL(self):
        glutInit()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glClearColor(1.0,1.0,1.0,1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        glMatrixMode(GL_MODELVIEW)
        
    def onWrongGuess(self):
        self.wrongGuesses += 1
        self.updateGL()
        if self.wrongGuesses >= 4:
            self.lose.emit()
        
    def onRightGuess(self):
        self.rightGuesses += 1
        self.updateGL()
        
    def onReset(self):
        self.wrongGuesses = 0
        self.rightGuesses = 0
        self.updateGL()
         
