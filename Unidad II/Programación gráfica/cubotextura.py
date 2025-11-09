from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

# Variables globales
texturas = []
angulo_x = 25
angulo_y = 30

def cargar_textura(ruta):
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

    import os
    base = r"E:\Universidad\Ing. Estadística e Informática\IV Semestre\Lenguajes de programación II\Unidad II\Programación gráfica"
    rutas = [os.path.join(base, f"cara{i}.png") for i in range(1, 7)]
    texturas = [cargar_textura(r) for r in rutas]

def dibujar_cubo():
    global angulo_x, angulo_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(angulo_x, 1, 0, 0)
    glRotatef(angulo_y, 0, 1, 0)

    # --- Caras del cubo ---
    caras = [
        (texturas[0], (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1)),  # frontal
        (texturas[1], (-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1)),  # trasera
        (texturas[2], (-1,  1, -1), ( 1,  1, -1), ( 1,  1,  1), (-1,  1,  1)),  # superior
        (texturas[3], (-1, -1, -1), ( 1, -1, -1), ( 1, -1,  1), (-1, -1,  1)),  # inferior
        (texturas[4], (-1, -1, -1), (-1, -1,  1), (-1,  1,  1), (-1,  1, -1)),  # izquierda
        (texturas[5], ( 1, -1, -1), ( 1, -1,  1), ( 1,  1,  1), ( 1,  1, -1))   # derecha
    ]

    for tex, v1, v2, v3, v4 in caras:
        glBindTexture(GL_TEXTURE_2D, tex)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3fv(v1)
        glTexCoord2f(1, 0); glVertex3fv(v2)
        glTexCoord2f(1, 1); glVertex3fv(v3)
        glTexCoord2f(0, 1); glVertex3fv(v4)
        glEnd()

    glFlush()

# 🕹️ Nueva función para mover con el teclado
def teclas_especiales(key, x, y):
    global angulo_x, angulo_y
    if key == GLUT_KEY_LEFT:
        angulo_y -= 5
    elif key == GLUT_KEY_RIGHT:
        angulo_y += 5
    elif key == GLUT_KEY_UP:
        angulo_x -= 5
    elif key == GLUT_KEY_DOWN:
        angulo_x += 5
    glutPostRedisplay()  # Redibuja

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cubo con texturas y control con teclado")
    inicializar()
    glutDisplayFunc(dibujar_cubo)
    glutSpecialFunc(teclas_especiales)  # Detecta teclas de flecha
    glutMainLoop()

if __name__ == "__main__":
    main()
