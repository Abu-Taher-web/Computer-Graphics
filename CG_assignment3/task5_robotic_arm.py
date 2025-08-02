from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Joint angles
shoulder_angle = 0.0
elbow_angle = 0.0
wrist_angle = 0.0

# Window dimensions
width, height = 800, 600


def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)


def draw_cube(size):
    half = size / 2.0
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-half, -half,  half)
    glVertex3f( half, -half,  half)
    glVertex3f( half,  half,  half)
    glVertex3f(-half,  half,  half)
    # Back face
    glVertex3f(-half, -half, -half)
    glVertex3f(-half,  half, -half)
    glVertex3f( half,  half, -half)
    glVertex3f( half, -half, -half)
    # Left face
    glVertex3f(-half, -half, -half)
    glVertex3f(-half, -half,  half)
    glVertex3f(-half,  half,  half)
    glVertex3f(-half,  half, -half)
    # Right face
    glVertex3f( half, -half, -half)
    glVertex3f( half,  half, -half)
    glVertex3f( half,  half,  half)
    glVertex3f( half, -half,  half)
    # Top face
    glVertex3f(-half,  half, -half)
    glVertex3f(-half,  half,  half)
    glVertex3f( half,  half,  half)
    glVertex3f( half,  half, -half)
    # Bottom face
    glVertex3f(-half, -half, -half)
    glVertex3f( half, -half, -half)
    glVertex3f( half, -half,  half)
    glVertex3f(-half, -half,  half)
    glEnd()


def draw_robot_arm():
    global shoulder_angle, elbow_angle, wrist_angle

    # Shoulder segment
    glPushMatrix()
    glRotatef(shoulder_angle, 0.0, 0.0, 1.0)
    glTranslatef(1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.0, 0.3, 0.3)
    draw_cube(1.0)
    glPopMatrix()

    # Elbow segment
    glTranslatef(1.0, 0.0, 0.0)
    glRotatef(elbow_angle, 0.0, 0.0, 1.0)
    glTranslatef(1.0, 0.0, 0.0)
    glPushMatrix()
    glScalef(2.0, 0.2, 0.2)
    draw_cube(1.0)
    glPopMatrix()

    # Wrist segment
    glTranslatef(1.0, 0.0, 0.0)
    glRotatef(wrist_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.5, 0.0, 0.0)
    glPushMatrix()
    glScalef(1.0, 0.1, 0.1)
    draw_cube(1.0)
    glPopMatrix()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Camera
    gluLookAt(3.0, 3.0, 5.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

    # Draw axes
    glBegin(GL_LINES)
    # X axis (red)
    glColor3f(1, 0, 0)
    glVertex3f(0,0,0)
    glVertex3f(2,0,0)
    # Y axis (green)
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,2,0)
    # Z axis (blue)
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,2)
    glEnd()

    # Draw robot
    glColor3f(0.8, 0.8, 0.8)
    draw_robot_arm()

    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global shoulder_angle, elbow_angle, wrist_angle
    step = 5.0
    if key == b'q':
        shoulder_angle = (shoulder_angle + step) % 360
    elif key == b'a':
        shoulder_angle = (shoulder_angle - step) % 360
    elif key == b'w':
        elbow_angle = (elbow_angle + step) % 360
    elif key == b's':
        elbow_angle = (elbow_angle - step) % 360
    elif key == b'e':
        wrist_angle = (wrist_angle + step) % 360
    elif key == b'd':
        wrist_angle = (wrist_angle - step) % 360
    elif key == b'\x1b':  # ESC
        sys.exit()
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"PyOpenGL Robot Arm")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == '__main__':
    main()
