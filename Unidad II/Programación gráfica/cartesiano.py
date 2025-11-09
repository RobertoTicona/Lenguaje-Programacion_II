import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def texto(x, y, string, font=GLUT_BITMAP_HELVETICA_12): # type: ignore
    """Función auxiliar para escribir texto en (x, y)"""
    glRasterPos2f(x, y)
    for ch in string:
        glutBitmapCharacter(font, ord(ch))

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)

    # Ejes
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)
    glVertex2f(0.0, -2.5)
    glVertex2f(0.0, 2.5)
    glEnd()

    # Marcas y números del eje X
    for x in range(-2, 3):
        if x != 0:
            glBegin(GL_LINES)
            glVertex2f(x, -0.05)
            glVertex2f(x, 0.05)
            glEnd()
            texto(x - 0.1, -0.2, str(x))

    # Marcas y números del eje Y
    for y in range(-2, 3):
        if y != 0:
            glBegin(GL_LINES)
            glVertex2f(-0.05, y)
            glVertex2f(0.05, y)
            glEnd()
            texto(-0.3, y - 0.05, str(y))

    # Dibujar función y = x^2
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-1.5, 1.5, 200):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    # Título o etiquetas
    glColor3f(1, 1, 0)
    texto(-2.9, 2.7, "Grafico: y = x^2", GLUT_BITMAP_HELVETICA_18) # type: ignore

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Plano cartesiano con texto - y = x^2")
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__ == "__main__":
    main()
