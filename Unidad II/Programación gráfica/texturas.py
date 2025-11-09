from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

# Variables globales
texturas = []
angulo_x = 25
angulo_y = 30

# ------------------ FUNCIONES ------------------

def cargar_textura(ruta):
    """Carga una imagen y la convierte en textura OpenGL"""
    imagen = Image.open(ruta)
    imagen = imagen.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = imagen.convert("RGB").tobytes()

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imagen.width, imagen.height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return tex_id


def inicializar():
    global texturas
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -5.0, 5.0)

    glEnable(GL_TEXTURE_2D)

    # Cargar una textura por cara
    rutas = [
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara1.png",
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara2.png",
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara3.png",
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara4.png",
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara5.png",
    r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\cara6.png"
    ]

    texturas = [cargar_textura(r) for r in rutas]


def dibujar_cubo():
    global angulo_x, angulo_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(angulo_x, 1, 1, 0)
    glRotatef(angulo_y, 0, 1, 0)

    # Cara frontal
    glBindTexture(GL_TEXTURE_2D, texturas[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1,  1)
    glEnd()

    # Cara trasera
    glBindTexture(GL_TEXTURE_2D, texturas[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1, -1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)
    glEnd()

    # Cara superior
    glBindTexture(GL_TEXTURE_2D, texturas[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1,  1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1,  1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1,  1)
    glEnd()

    # Cara inferior
    glBindTexture(GL_TEXTURE_2D, texturas[3])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1, -1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1, -1,  1)
    glEnd()

    # Cara izquierda
    glBindTexture(GL_TEXTURE_2D, texturas[4])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f(-1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)
    glEnd()

    # Cara derecha
    glBindTexture(GL_TEXTURE_2D, texturas[5])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f(1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f(1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(1,  1, -1)
    glEnd()

    glFlush()


def rotar():
    """Función de rotación continua"""
    global angulo_x, angulo_y
    angulo_x += 0.5
    angulo_y += 0.8
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cubo con 6 texturas y rotacion")
    inicializar()
    glutDisplayFunc(dibujar_cubo)
    glutIdleFunc(rotar)  # Actualiza continuamente
    glutMainLoop()

if __name__ == "__main__":
    main()
