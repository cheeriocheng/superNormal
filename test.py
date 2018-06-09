import glfw
import OpenGL.GL as gl
import OpenGL.GLU as glu


def main():

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

    def Cube():
        gl.glBegin(gl.GL_LINES)
        for edge in edges:
            for vertex in edge:
                gl.glVertex3fv(vertices[vertex])
        gl.glEnd()

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

    glu.gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    gl.glTranslatef(0.0,0.0, -20)

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
        
       
        gl.glRotatef(glfw.get_time() * 50, 0, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
        Cube()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()