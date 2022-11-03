import pygame as pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *


def square():
    glBegin(GL_POLYGON)
    glVertex2f(0, -0.5)
    glVertex2f(-0.2, .7)
    glVertex2f(0, .5)
    glVertex2f(.2, .7)
    glEnd()
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0, 0, .5)
        square()
        pygame.display.flip()
        pygame.time.wait(10)

main()
