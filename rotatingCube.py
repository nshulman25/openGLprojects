import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

vertices = (
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1)
)

edges = (
    (0, 1), (2, 3),  # front face
    (4, 5), (6, 7),  # back face
    (4, 5), (1, 0),  # right face
    (7, 6), (2, 3),  # left face
    (4, 0), (3, 7),  # top face
    (5, 1), (2, 6)  # bottom face
)

colors = (
    (0, 0, 0),  # this gets skiped over
    (0, 1, 0),  # front face (green)
    (0, 0, 1),  # back face (blue)
    (1, 0, 0),  # right face (red)
    (1, 1, 0),  # left facw (yellow)
    (0, 1, 1),  # top face (teal)
    (1, 0, 1)  # bottom face (magenta)
)

# draws each vertex and the connects them as QUADS
def cube():
    glBegin(GL_QUADS)
    x = 0
    y = 0

    # loops through every edge
    for edge in edges:

        # changes the color being drawn every time a face is completed
        if y % 2 == 0:
            x = x + 1
        glColor3fv(colors[x])
        y = y + 1

        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # comapres the depth of objects in the framebuffer, so surface are not see through.
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(50)


main()
