#-------------------------------------------------------------------------------
# Name: 521140S：4 Computer Graphics (2022) Programming Assignment 0 
# Purpose: Environment setting for Python and OpenGL (Teapot version)
#-------------------------------------------------------------------------------

import OpenGL.GLUT as oglut
import OpenGL.GL as gl
import OpenGL.GLU as glu

class GlutWindow(object):

    def __init__(self):
        oglut.glutInit()
        
        # Initialize display mode
        oglut.glutInitDisplayMode(oglut.GLUT_RGBA | oglut.GLUT_DOUBLE | oglut.GLUT_DEPTH)
        
        # 1. Window size setup
        oglut.glutInitWindowSize(800, 480)
        oglut.glutCreateWindow(b"CG_Programming_Assignment_0 - Teapot")
        oglut.glutDisplayFunc(self.display)
        oglut.glutReshapeFunc(self.resize)  

    def ogl_draw(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        
        # 2. Set polygon mode to line (wireframe)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)

        # 3. Set the camera/viewpoint
        glu.gluLookAt(4.0, 3.0, -3.0,  # eye position
                      0.0, 0.0, 0.0,   # look-at point
                      0.0, 1.0, 0.0)   # up vector
        
        # 4. Render a solid teapot (instead of cube)
        oglut.glutSolidTeapot(0.8)  # 0.8 is the size (scale) of the teapot

    def display(self):    
        self.ogl_draw()
        oglut.glutSwapBuffers()
        
    def resize(self, Width, Height):
        gl.glViewport(0, 0, Width, Height)
        glu.gluPerspective(45.0, float(Width) / float(Height), 0.1, 1000.0)        

    def run(self):
        oglut.glutMainLoop()


if __name__ == "__main__":
    win = GlutWindow()
    win.run()
