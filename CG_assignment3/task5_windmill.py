from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle_hub = 0


def init():
    glClearColor(0.6, 0.8, 1.0, 1.0)  # Sky blue
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Light settings
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])


def draw_windmill():
    global angle_hub

    glPushMatrix()
    # Draw base
    glColor3f(0.5, 0.3, 0.1)
    glTranslatef(0, -1.5, 0)
    glPushMatrix()
    glScalef(0.5, 3, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    # Draw hub and spin blades around the Z-axis
    glTranslatef(0, 3, 0)
    glRotatef(angle_hub, 0, 0, 1)  # Correct axis: Z

    glColor3f(0.8, 0.8, 0.8)
    glutSolidSphere(0.2, 20, 20)

    # Draw 3 fixed-orientation blades around hub
    for i in range(3):
        glPushMatrix()
        glRotatef(i * 120, 0, 0, 1)  # Blade offset angle
        glTranslatef(0, 0.8, 0)       # Offset from hub
        glPushMatrix()
        glScalef(0.1, 1.5, 0.1)
        glColor3f(0.9, 0.1, 0.1)
        glutSolidCube(1)
        glPopMatrix()

        # Bird nest on first blade
        if i == 0:
            glTranslatef(0, 0.8, 0)
            glColor3f(0.4, 0.2, 0.1)
            glutSolidSphere(0.1, 10, 10)

        glPopMatrix()

    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(4, 3, 6, 0, 0, 0, 0, 1, 0)

    draw_windmill()

    glutSwapBuffers()


def idle():
    global angle_hub
    angle_hub += 0.5
    if angle_hub > 360:
        angle_hub -= 360
    glutPostRedisplay()


def reshape(w, h):
    if h == 0:
        h = 1
    aspect = w / h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 1, 100)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Windmill - Hierarchical Model")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
