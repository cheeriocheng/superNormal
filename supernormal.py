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

RESOLUTION = 20 #only deal with the chairs at the same resolution 
CUBE_SIZE = 2 
THRESHOLD = 0.3

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


def averageChairs():
    occupiedCubes = []
     #load all the models with the same grid  
    models = load_json.load_folder('models',RESOLUTION )

    # an empty list for holding chair models 
    voxel_matrix = np.zeros((RESOLUTION ,RESOLUTION, RESOLUTION))
    # adding up chairs 
    for chair in models:
        #for each vox written in json file 
        for c in chair: 
            voxel_matrix[c[0],c[1],c[2]] += 1 
    voxel_matrix = np.array(voxel_matrix)/(len(models))
    print("averaging {} chairs".format(len(models)))
    # create a list of solid cells          
    for x in range(RESOLUTION): 
        for y in range(RESOLUTION): 
            for z in range(RESOLUTION): 
                v = voxel_matrix[x,y,z]
                # print("{},{},{}.{}".format(x,y,z,v))
                if v > THRESHOLD:
                    occupiedCubes.append([x,y,z])

    return occupiedCubes 



def exportForMatlab(cubes):
    cubes_x =[]
    cubes_y =[]
    cubes_z =[]
    for c in cubes:
        cubes_x.append(c[0])
        cubes_y.append(c[1])
        cubes_z.append(c[2])
    
    with open('{}_cube_coordinates.txt'.format(RESOLUTION), 'w') as file:
        file.write('solidX = {}; \n'.format(cubes_x))
        file.write('solidY = {}; \n'.format(cubes_y))
        file.write('solidZ = {};'.format(cubes_z))

    print('Wrote cube coordinates.')



def main():

    # Initialize the library
    if not glfw.init():
        return

    display = [640, 480]
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(display[0], display[1], "super normal", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    glu.gluPerspective(45, (display[0]/display[1]), 0.1, 400.0)
    glu.gluLookAt(- RESOLUTION*CUBE_SIZE/2, RESOLUTION*CUBE_SIZE/2, RESOLUTION*CUBE_SIZE*2, RESOLUTION*CUBE_SIZE/2 , RESOLUTION*CUBE_SIZE/2 ,0, 0,1,0)
    
    # gl.glRotatef(-math.radians(90), 0.0, 1.0, 0.0);
    # glRotatef(-xAngle, 1.0f, 0.0f, 0.0f);
    # gl.glTranslatef(- RESOLUTION*CUBE_SIZE/2, -RESOLUTION*CUBE_SIZE/2, - RESOLUTION*CUBE_SIZE*2) #-60-RESOLUTION*4
    gl.glColor4f(1,1,1,1)


    cubes = averageChairs() 

    exportForMatlab(cubes)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
       
        # gl.glRotatef(glfw.get_time() , 0, 1, 1)
        # gl.glRotatef(math.radians(30), 1, 1, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        #render the chairs as is 
        # gl.glColor4f(1,1,1,1)
        # for chair in models:
        #     for c in chair: 
        #         gl.glTranslate( CUBE_SIZE*c[0] , CUBE_SIZE*c[1] , CUBE_SIZE*c[2] )
        #         drawCube()
        #         gl.glTranslate( -CUBE_SIZE*c[0] , -CUBE_SIZE*c[1] , -CUBE_SIZE*c[2] )

        #rendered the averaged chairs 
        for c in cubes:

            gl.glTranslate( CUBE_SIZE*c[0] , CUBE_SIZE*c[1] , CUBE_SIZE*c[2] )
            drawCube()
            gl.glTranslate( -CUBE_SIZE*c[0] , -CUBE_SIZE*c[1] , -CUBE_SIZE*c[2] )


        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()