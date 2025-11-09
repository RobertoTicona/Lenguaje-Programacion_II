from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angulo = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar rotación
    
    glRotate(angulo, 0.0, 0.0, 1.0)
    
    # glColor3f(0.0, 1.0, 0.0)  # Color amarillo
    glBegin(GL_TRIANGLES)  
    glColor3f(1.0, 0.0, 0.0); glVertex2f(0.0, 0.5)    # Vértice superior
    glColor3f(0.0, 1.0, 0.0); glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glColor3f(0.0, 0.0, 1.0); glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glEnd()

    glFlush()
    
def special_keys(key, x, y):
    global angulo
    if key == GLUT_KEY_LEFT: # Flecha izquierda
        angulo += 5
    elif key == GLUT_KEY_RIGHT:
        angulo -= 5
    glutPostRedisplay() # Redibujar la escena
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotacion con teclado")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__=="__main__":
    main()

