from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

texture = None

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
    global texture
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -5.0, 5.0)

    glEnable(GL_TEXTURE_2D)
    texture = cargar_textura(r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica\figura.png")


def dibujar_cubo():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(25, 1, 1, 0)

    # --- Cara frontal (con textura)
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1, -1,  1)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1,  1,  1)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1,  1)
    glEnd()

    # --- Otras caras (colores sólidos)
    glBindTexture(GL_TEXTURE_2D, 0)

    # Cara trasera (verde)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f( 1,  1, -1)
    glVertex3f( 1, -1, -1)
    glEnd()

    # Cara superior (azul)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1,  1)
    glVertex3f( 1,  1,  1)
    glVertex3f( 1,  1, -1)
    glEnd()

    # Cara inferior (amarilla)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1,  1)
    glVertex3f(-1, -1,  1)
    glEnd()

    # Cara izquierda (magenta)
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    glEnd()

    # Cara derecha (cyan)
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(1, -1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1,  1,  1)
    glVertex3f(1, -1,  1)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cubo 3D con textura (OpenGL)")
    inicializar()
    glutDisplayFunc(dibujar_cubo)
    glutMainLoop()


if __name__ == "__main__":
    main()

