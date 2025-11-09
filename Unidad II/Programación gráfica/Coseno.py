import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glPointSize(5)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)  # Vista ortográfica 2D

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-4.5, 0.0)
    glVertex2f(4.5, 0.0)
    glVertex2f(0.0, -4.5)
    glVertex2f(0.0, 4.5)
    glEnd()
    
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-4.0, 4.0, 200):
        y = np.cos(x)
        glVertex2f(x, y)
    glEnd()

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
