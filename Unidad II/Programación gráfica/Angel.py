from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glPointSize(5)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_triangulo():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_STRIP)  
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.7, -0.1)
    glVertex2f(-0.7, 0.1)
    glVertex2f(-0.5, 0.1)
    glVertex2f(-0.5, -0.1)
    glEnd()
    
    glBegin(GL_LINE_STRIP)  
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.7, 0.0)
    glVertex2f(-0.5, 0.0)
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.4, -0.1)
    glVertex2f(-0.4, 0.1)
    glVertex2f(-0.2, -0.1)
    glVertex2f(-0.2, 0.1)
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.1, 0.1)
    glVertex2f(-0.1, 0.1)
    glVertex2f(-0.1, -0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.1, 0.0)
    glVertex2f(-0.1, 0.0)
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.4, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, -0.1)
    glVertex2f(0.4, -0.1)
    glEnd()
    
    glBegin(GL_LINE_STRIP)  
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.2, 0.0)
    glVertex2f(0.4, 0.0)
    glEnd()
    
    glBegin(GL_LINE_STRIP)  
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(0.5, 0.1)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.7, -0.1)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Triangulo de puntos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutMainLoop()

if __name__=="__main__":
    main()

