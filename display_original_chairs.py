'''
render the chair and display for 5 min each
'''
import glfw
import OpenGL.GL as gl
import OpenGL.GLU as glu
import average_chair
import math 
import numpy as np 
import load_json
import time 

from platos_flood import platos_flood


import pprint

RESOLUTION = 60 #only deal with the chairs at the same resolution 
CUBE_SIZE = 2 



def drawCube():
    vertices= np.array([\
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
        ])

    edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
    )

    gl.glBegin(gl.GL_LINES)
    for edge in edges:
        for vertex in edge:
            gl.glVertex3fv(vertices[vertex])
    gl.glEnd()

def main():

    models = load_json.load_folder('models',RESOLUTION )

    # Initialize the library
    if not glfw.init():
        return

    display = [480, 480]
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(display[0], display[1], "super normal", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    glu.gluPerspective(45, (display[0]/display[1]), 0.1, RESOLUTION*6)
    # glu.gluLookAt(- RESOLUTION*CUBE_SIZE/2, RESOLUTION*CUBE_SIZE/2, RESOLUTION*CUBE_SIZE*2, RESOLUTION*CUBE_SIZE/2 , RESOLUTION*CUBE_SIZE/2 ,0, 0,1,0)
    glu.gluLookAt( RESOLUTION*CUBE_SIZE*1.2 , RESOLUTION*CUBE_SIZE/2*1.2, RESOLUTION*CUBE_SIZE*2*1.2, 0 , RESOLUTION*CUBE_SIZE/2 ,0, 0,1,0)

    
    # gl.glRotatef(-math.radians(90), 0.0, 1.0, 0.0);
    # glRotatef(-xAngle, 1.0f, 0.0f, 0.0f);
    # gl.glTranslatef(- RESOLUTION*CUBE_SIZE/2, -RESOLUTION*CUBE_SIZE/2, - RESOLUTION*CUBE_SIZE*2) #-60-RESOLUTION*4
    gl.glColor4f(1,1,1,1)

    print("Rendering...")

    ind = 0 
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
       
        # gl.glRotatef(glfw.get_time() , 0, 1, 1)
        # gl.glRotatef(math.radians(45), 1, 1, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        # render the chairs as is 
        
        # for chair in models:
        for c in models[ind]: 
            gl.glTranslate( CUBE_SIZE*c[0] , CUBE_SIZE*c[1] , CUBE_SIZE*c[2] )
            drawCube()
            gl.glTranslate( -CUBE_SIZE*c[0] , -CUBE_SIZE*c[1] , -CUBE_SIZE*c[2] )

        #rendered the averaged chairs 
        # for c in cubes:

        #     gl.glTranslate( CUBE_SIZE*c[0] , CUBE_SIZE*c[1] , CUBE_SIZE*c[2] )
        #     drawCube()
        #     gl.glTranslate( -CUBE_SIZE*c[0] , -CUBE_SIZE*c[1] , -CUBE_SIZE*c[2] )

        ind += 1
        time.sleep(5) 
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
