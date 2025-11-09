import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glPointSize(5)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)  # Vista ortográfica 2D
    
def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)
    glVertex2f(0.0, -2.5)
    glVertex2f(0.0, 2.5)
    glEnd()
    
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-1.5, 1.5, 200):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    glRasterPos2f(0.03, -0.12)
    for ch in "0":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(0.5, -0.12)
    for ch in "0.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(1.0, -0.12)
    for ch in "1":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(1.5, -0.12)
    for ch in "1.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(2.0, -0.12)
    for ch in "2":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(2.5, -0.12)
    for ch in "2.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(-0.5, -0.12)
    for ch in "-0.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(-1.0, -0.12)
    for ch in "-1":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(-1.5, -0.12)
    for ch in "-1.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(-2.0, -0.12)
    for ch in "-2":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(-2.5, -0.12)
    for ch in "-2.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, 0.5)
    for ch in "0.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, 1.0)
    for ch in "1":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(0.03, 1.5)
    for ch in "1.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, 2.0)
    for ch in "2":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, 2.5)
    for ch in "2.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, -0.5)
    for ch in "-0.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, -1.0)
    for ch in "-1":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    
    glRasterPos2f(0.03, -1.5)
    for ch in "-1.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, -2.0)
    for ch in "-2":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glRasterPos2f(0.03, -2.5)
    for ch in "-2.5":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
        
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Ecuacion cuadratica")
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
