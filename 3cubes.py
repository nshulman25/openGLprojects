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

#dispalys the orgin lines
def orgins():
    #x axis
    glColor3f(1.0,0.0,0.0) #red x
    glBegin(GL_LINES)
    glVertex3f(-4.0, 0.0, 0.0)
    glVertex3f(4.0, 0.0, 0.0)
    glEnd()

    #y axis 
    glColor3f(0.0,1.0,0.0) #green y
    glBegin(GL_LINES)
    glVertex3f(0.0, -4.0, 0.0)
    glVertex3f(0.0, 4.0, 0.0)
    glEnd()
 
    #z axis
    glColor3f(0.0,0.0,1.0); #blue z
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0 ,-4.0 )
    glVertex3f(0.0, 0.0 ,4.0 )
    glEnd()

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
    rotate_y = 0
    rotate_x = 0

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # comapres the depth of objects in the framebuffer, so surface are not see through.
    glEnable(GL_DEPTH_TEST)

    # settings to adjust the camera perspective
    gluPerspective(45, (display[0]/display[1]), 6, 50.0)
    gluLookAt(0,10,20,0,0,0,0,1,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # allows control of camera perspective
            # use directional keys to move camera perspective
            # q moves away from viewer
            # e moces towards viewer
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_q:
                    glTranslatef(0,0,-1)
                if event.key == pygame.K_e:
                    glTranslatef(0,0,1)
                
                # rotates the first cube according to the key press
                # r = counter clockwise on the y axis
                # i = clockwise on the y axis
                # u = clockwise on the x axis
                # d = counter clockwise on the x axis
                if event.key == pygame.K_r:
                    rotate_y -= 30
                if event.key == pygame.K_i:
                    rotate_y += 30
                if event.key == pygame.K_u:
                    rotate_x -= 30
                if event.key == pygame.K_d:
                    rotate_x += 30


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        orgins()
        glPopMatrix()

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(3,0,0)
        glRotatef(rotate_y,0,1,0)
        glRotatef(rotate_x,1,0,0)
        cube()
        glPopMatrix()

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(6,0,0)
        cube()
        glTranslatef(0,0,-3)
        cube()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        
main()
