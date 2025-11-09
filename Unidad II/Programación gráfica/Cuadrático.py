from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glPointSize(5)  # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, -3.0, 3.0)  # Vista ortográfica 2D

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)  
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)
    glVertex2f(0.0, -2.5)
    glVertex2f(0.0, 2.5)
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-1.5, 2.25)
    glVertex2f(-1.0, 1.0)
    glVertex2f(-0.5, 0.25)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.5, 0.25)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.5, 2.25)
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

