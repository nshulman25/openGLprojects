import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

light_vertices = (
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1)
)

light_edges = (
    (0, 1), (2, 3),  # front face
    (4, 5), (6, 7),  # back face
    (4, 5), (1, 0),  # right face
    (7, 6), (2, 3),  # left face
    (4, 0), (3, 7),  # top face
    (5, 1), (2, 6)  # bottom face
)

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
    #(0, 1), (2, 3),  # front face
    (4, 5), (6, 7),  # back face
    #(4, 5), (1, 0),  # right face
    #(7, 6), (2, 3),  # left face
    (4, 0), (3, 7),  # top face
    (5, 1), (2, 6)  # bottom face
)
roof_vertices = (
    (1, 1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, 1, 1),
    (0, 2, 1),
    (0, 2, -1),
)
roof_edges = (
    (0, 3, 4), # front face
    (1, 5, 2), # back face
    (0,1), (5,4), # right face
    (3,2), (5,4) # left face
)
door_vertices = (
    (-1,1,1),
    (-1,-1,1),
    (-0.3,-1,1),
    (-0.3,1,1),
    (1, 1, 1),
    (1, -1, 1),
    (0.3, -1, 1),
    (0.3, 1, 1),
    (-0.3,0,1),
    (0.3,0,1)
    
)
door_edges = (
    (0, 1), (2, 3), 
    (4,5), (6,7),
    (0,8), (9,4)
)
window_vertices = (
    (-1,1,0),
    (-1,-0.5,0),
    (-0.5,-0.5,0),
    (-0.5,1,0),
    (-1, -1, 0),
    (0.5, -1, 0),
    (0.5, -0.5, 0),
    (1,-1,0),
    (1,0.5,0),
    (0.5,0.5,0),
    (1,1,0),
    (-0.5,0.5,0)

    
)
window_edges = (
    (0, 1), (2, 3), # quad one
    (1,4), (5,6), #quad two
    (5,7), (8,9), # quad three
    (8,10), (3,11) #quad four
)
mailbox_vertices = (
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1)
)
mailbox_edges = (
    (0, 1), (2, 3),  # front face
    (4, 5), (6, 7),  # back face
    (4, 5), (1, 0),  # right face
    (7, 6), (2, 3),  # left face
    (4, 0), (3, 7),  # top face
    (5, 1), (2, 6)  # bottom face
)

# draws the mailbox structure
def mailbox():
    
    # draws the box
    glColor3f(0.1, 0.1, 0.1) 
    glScale(.3,.2,.2)
    glBegin(GL_QUADS)
  
    # loops through every edge
    for edge in mailbox_edges:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(mailbox_vertices[vertex])
    glEnd()

    # draws the post
    glColor3f(0.23, 0.17, 0.14) 
    glTranslate(0,-2.01,0)
    glScale(.5,3,.4)
    glBegin(GL_QUADS)
  
    # loops through every edge
    for edge in mailbox_edges:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(mailbox_vertices[vertex])
    glEnd()

# draws the roof structure takes color argument
def roof(color):
    
    # if color statment
    if color == "brown":
        glColor3f(0.69, 0.48, 0.35)
    if color == "blue":
        glColor3f(0.24, 0.49, 0.8)
    if color == "red":
        glColor3f(0.8, 0.27, 0.24)

    # draws sides of the roof
    glBegin(GL_TRIANGLES)
    
    # loops through every edge
    for edge in roof_edges[:2]:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(roof_vertices[vertex])
    glEnd()

    # draws the base of the roof
    glColor3f(0.25,0.25,0.25) #grey
    glBegin(GL_QUADS)
    
    # loops through every edge
    for edge in roof_edges[-4:]:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(roof_vertices[vertex])
    glEnd()

# draws the house structure
def house(color):

    # draws house shape
    glBegin(GL_QUADS) 
    x = 0

    # loops through every edge to make the house shape
    for edge in edges:
        if color == "brown":
            glColor3f(0.69, 0.48, 0.35)
            # changes the color being drawn every time a face is completed
            if x == 4 or x == 5:
                glColor3f(0.33,0.33,0.33)
        if color == "blue":
            glColor3f(0.24, 0.49, 0.8)
            # changes the color being drawn every time a face is completed
            if x == 4 or x == 5:
                glColor3f(0.33,0.33,0.33)
        if color == "red":
            glColor3f(0.8, 0.27, 0.24)
            # changes the color being drawn every time a face is completed
            if x == 4 or x == 5:
                glColor3f(0.33,0.33,0.33)
        x = x + 1
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    # draws door frame
    if color == "brown":
        glColor3f(0.69, 0.48, 0.35)
    if color == "blue":
        glColor3f(0.24, 0.49, 0.8)
    if color == "red":
        glColor3f(0.8, 0.27, 0.24)
    glBegin(GL_QUADS)
  
    # loops through every edge to make the door frame
    for edge in door_edges:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(door_vertices[vertex])
    glEnd()

#draws a window frame
def windows(color):
    
    # draws windows frame
    if color == "brown":
        glColor3f(0.69, 0.48, 0.35)
    if color == "blue":
        glColor3f(0.24, 0.49, 0.8)
    if color == "red":
        glColor3f(0.8, 0.27, 0.24)
    glBegin(GL_QUADS)
  
    # loops through every edge to make the door frame
    for edge in window_edges:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(window_vertices[vertex])
    glEnd()

#draws physical door
def door():

    # door varaibles
    door_v = (
        (0.3, 0),
        (0.3, -1),
        (-0.3, -1),
        (-0.3, 0)
    )

    door_e = (
        (0, 1), (2, 3),
    )

    # draws door
    glColor3f(0.28, 0.41, 0.84)
    glBegin(GL_QUADS)
  
    # loops through every edge to make the door 
    for edge in door_e:
        
        # loops through every vertex and draws it
        for vertex in edge:
            glVertex2fv(door_v[vertex])
    glEnd()

# draws a single yellow dash for the road
def dashes():
    glColor3f(0.98, 0.93, 0.01) 
    glBegin(GL_QUADS)
    glVertex3f(50,0.02,.2)
    glVertex3f(50,0.02,-.2)
    glVertex3f(49,0.02,-.2)
    glVertex3f(49,0.02,.2)
    glEnd()

#draws the grass on the ground and places a road in the middle
def ground():

    # draws grass with texture
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(50.0, 0.0, 50.0) 	
    glTexCoord2f(8.0, 0.0)
    glVertex3f(50.0, 0.0, -50.0)
    glTexCoord2f(8.0, 8.0)
    glVertex3f(-50.0, 0.0, -50.0)
    glTexCoord2f(0.0, 8.0)
    glVertex3f(-50.0, 0.0, 50.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # draw road
    glColor3f(0,0,0) 
    glBegin(GL_QUADS)
    glVertex3f(50,0.01,3)
    glVertex3f(50,0.01,-3)
    glVertex3f(-50,0.01,-3)
    glVertex3f(-50,0.01,3)
    glEnd()

    # draws multiple dashes on the road
    for i in range(20):
        dashes()
        glTranslate(-5,0,0)

# draws a pine tree
def tree():
    cylinder = gluNewQuadric()

    # trunk
    glPushMatrix()
    glMatrixMode(GL_MODELVIEW)
    glRotatef(90,1,0,0)
    glColor3f(0.29, 0.19, 0.14)
    gluCylinder(cylinder,1,1,5,8,1)
    glPopMatrix()

    # each layer of leaves
    glPushMatrix()
    glMatrixMode(GL_MODELVIEW)
    glRotatef(90,1,0,0)
    glTranslatef(0,0,-2)
    glColor3f(0.21, 0.29, 0.14)
    gluCylinder(cylinder,0,2,4,8,1)
    glPopMatrix()

    glPushMatrix()
    glMatrixMode(GL_MODELVIEW)
    glRotatef(90,1,0,0)
    glTranslatef(0,0,-3)
    glColor3f(0.21, 0.29, 0.14)
    gluCylinder(cylinder,0,1.5,3,8,1)
    glPopMatrix()

    glPushMatrix()
    glMatrixMode(GL_MODELVIEW)
    glRotatef(90,1,0,0)
    glTranslatef(0,0,-4)
    glColor3f(0.21, 0.29, 0.14)
    gluCylinder(cylinder,0,1,2,8,1)
    glPopMatrix()
    
def light():
    glBegin(GL_QUADS)
    x = 0
    y = 0

    # loops through every edge
    glNormal3d(0, 0, 1)
    for edge in light_edges:

        # loops through every vertex and draws it
        for vertex in edge:
            glVertex3fv(light_vertices[vertex])
    glEnd()

    ambientLight = ( 0.2, 0.2, 0.2, 1.0 )
    diffuseLight = ( 0.8, 0.8, 0.8, 1.0)
    specularLight = ( 0.5, 0.5, 0.5, 1.0 )
    position = (0, 0, 0, 1.0 )

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight)
    glLightfv(GL_LIGHT0, GL_POSITION, position)

# does texturing work
class Material:

    def __init__(self):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D,self.texture)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        image = pygame.image.load("grass.png").convert_alpha()
        image_width, image_height = image.get_rect().size
        image_data = pygame.image.tostring(image, "RGB")
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image_width, image_height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)


    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D,self.texture)
    
    def end(self):
        glDeleteTextures(1,(self.texture,))

def main():
    rotate_door = 0
    translate_door = 0

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # comapres the depth of objects in the framebuffer, so surface are not see through.
    glEnable(GL_DEPTH_TEST)
    glShadeModel (GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    grass_texture = Material()

    # settings to adjust the camera perspective
    gluPerspective(45, (display[0]/display[1]), .1, 50.0)
    gluLookAt(0,10,20,0,0,0,0,1,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # allows control of camera perspective
            # use directional keys to move camera perspective
            # e moves away from viewer
            # q moves towards viewer
            # d rotates counter clockwise
            # a rotates clockwise
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_q:
                    glTranslatef(0,0,-1)
                if event.key == pygame.K_e:
                    glTranslatef(0,0,1)
                if event.key == pygame.K_a:
                    glRotatef(10,0,1,0)
                if event.key == pygame.K_d:
                    glRotatef(-10,0,1,0)
                if event.key == pygame.K_z:
                    glDisable(GL_LIGHT0)
                if event.key == pygame.K_o:
                    glEnable(GL_LIGHT0)
                
                # keys for rotating certain objects
                # o = open door
                # c = close door
                # u = clockwise on the x axis
                # d = counter clockwise on the x axis
                if event.key == pygame.K_o:
                    if translate_door != -0.3:
                        rotate_door -= 15
                        translate_door -= .05
                if event.key == pygame.K_c:
                    if translate_door <= 0:
                        rotate_door += 15
                        translate_door += .05
                # if event.key == pygame.K_u:
                #     rotate_x -= 30
                # if event.key == pygame.K_d:
                #     rotate_x += 30


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(5,0,5)
        glRotatef(180,0,1,0)
        house("brown")
        glTranslate(1,0,0)
        glRotatef(90,0,1,0)
        windows("brown")
        glTranslate(0,0,-2)
        windows("brown")
        glTranslate(0,0,1)
        roof("brown")
        glTranslate(-1.5,0,-1)
        mailbox()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(5,0,4)
        glRotatef(rotate_door,0,1,0)
        glTranslatef(0,0,translate_door)
        door()
        glPopMatrix()


        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(-5,.5,7)
        glRotatef(180,0,1,0)
        glScalef(1.5,1.5,1.5)
        house("red")
        glTranslate(1,0,0)
        glRotatef(90,0,1,0)
        windows("red")
        glTranslate(0,0,-2)
        windows("red")
        glTranslate(0,0,1)
        roof("red")
        glTranslate(-1.5,-0.25,-1)
        glScalef(.75,.75,.75)
        mailbox()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-5,.5,5.5)
        glScalef(1.5,1.5,1.5)
        door()
        glPopMatrix()

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(-5,0,-5)
        house("brown")
        glTranslate(1,0,0)
        glRotatef(90,0,1,0)
        windows("brown")
        glTranslate(0,0,-2)
        windows("brown")
        glTranslate(0,0,1)
        roof("brown")
        glTranslate(-1.5,0,-1)
        mailbox()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-1.5,3,-5)
        tree()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-5,0,-4)
        door()
        glPopMatrix()

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(5,0,-5)
        house("blue")
        glTranslate(1,0,0)
        glRotatef(90,0,1,0)
        windows("blue")
        glTranslate(0,0,-2)
        windows("blue")
        glTranslate(0,0,1)
        roof("blue")
        glTranslate(-1.5,0,-1)
        mailbox()
        glPopMatrix()

        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(5,0,-5)
        glScale(.5,.5,.5)
        light()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(5,0,-4)
        door()
        glPopMatrix()

        glPushMatrix()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0,-1.01,0)
        ground()
        glPopAttrib()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        
main()
