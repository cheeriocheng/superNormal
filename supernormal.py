'''
average and render the chair
'''
import glfw
import OpenGL.GL as gl
import OpenGL.GLU as glu
import load_json
import math 
import numpy as np 

import pprint

RESOLUTION = 60 #only deal with the chairs at the same resolution 
MATRIX_SIZE = RESOLUTION + 1 

def drawCube():
    vertices= (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )
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

    # Initialize the library
    if not glfw.init():
        return

    display = [640, 480]
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(display[0], display[1], "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    cubeSize = 2 

    glu.gluPerspective(45, (display[0]/display[1]), 0.1, 400.0)
    gl.glTranslatef(- RESOLUTION*cubeSize/2, -RESOLUTION*cubeSize/2, - RESOLUTION*cubeSize*2) #-60-RESOLUTION*4
    gl.glColor4f(1,1,1,1)

    #load all the models with the same grid  
    models = load_json.load_folder('models',RESOLUTION )
    
    # an empty list for holding chair models 
    voxel_matrix = np.zeros((MATRIX_SIZE ,MATRIX_SIZE, MATRIX_SIZE))
    # adding up chairs 
    for chair in models:
        #for each vox written in json file 
        for c in chair: 
            voxel_matrix[c[0],c[1],c[2]] += 1 
    voxel_matrix = np.array(voxel_matrix)/(len(models))

    cubes = []
    # create a list of solid cells          
    for x in range(MATRIX_SIZE): 
        for y in range(MATRIX_SIZE): 
            for z in range(MATRIX_SIZE): 
                v = voxel_matrix[x,y,z]
                # print("{},{},{}.{}".format(x,y,z,v))
                if v > 0.5:
                    cubes.append([x,y,z,v])

    offsetX = 0 # RESOLUTION 

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        # width, height = glfw.get_framebuffer_size(window)
        # ratio = width / float(height)
        # gl.glViewport(0, 0, width, height)
        # gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # gl.glMatrixMode(gl.GL_PROJECTION)
        # gl.glLoadIdentity()
        # gl.glOrtho(-ratio, ratio, -1, 1, 1, -1)
        # gl.glMatrixMode(gl.GL_MODELVIEW)
        # gl.glLoadIdentity()
        # gl.glRotatef(glfw.get_time() * 50, 0, 1, 1)
        # gl.glBegin(gl.GL_TRIANGLES)
        # gl.glColor3f(1, 0, 0)
        # gl.glVertex3f(-0.6, -0.4, 0)
        # gl.glColor3f(0, 1, 0)
        # gl.glVertex3f(0.6, -0.4, 0)
        # gl.glColor3f(0, 0, 1)
        # gl.glVertex3f(0, 0.6, 0)
        # gl.glEnd()
       
        # gl.glRotatef(glfw.get_time() , 0, 1, 1)
        gl.glRotatef(math.radians(30), 1, 1, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        #render the chairs as is 
        # gl.glColor4f(1,1,1,1)
        # for chair in models:
        #     for c in chair: 
        #         gl.glTranslate( cubeSize*c[0] , cubeSize*c[1] , cubeSize*c[2] )
        #         drawCube()
        #         gl.glTranslate( -cubeSize*c[0] , -cubeSize*c[1] , -cubeSize*c[2] )

        for c in cubes:
            gl.glTranslate( cubeSize*c[0] , cubeSize*c[1] , cubeSize*c[2] )
            drawCube()
            gl.glTranslate( -cubeSize*c[0] , -cubeSize*c[1] , -cubeSize*c[2] )


        # #render the averaged chair         
        # for x in range(MATRIX_SIZE): 
        #     for y in range(MATRIX_SIZE): 
        #         for z in range(MATRIX_SIZE): 
        #             v = voxel_matrix[x,y,z]
        #             # print("{},{},{}.{}".format(x,y,z,v))
        #             if v<0.5:
        #                 continue
        #             else:
        #                 gl.glTranslate( cubeSize*(x + offsetX), cubeSize*y , cubeSize*z )
        #                 Cube()
        #                 gl.glTranslate( -cubeSize*(x + offsetX), -cubeSize*y , -cubeSize*z )




        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()