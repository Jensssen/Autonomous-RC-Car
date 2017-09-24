import pygame
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('192.168.178.30', 8000)) #Adolf-Wagner Laptop
s.bind(('192.168.2.67', 8000)) # Area51 pi
#s.bind(('127.0.0.1', 8000)) #LocalHost
print("Lisstening for connections...")
s.listen(1)
connection, address = s.accept()
print("Connected to client", address)


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Define some variables
var_speed = 0
speed = 0
angle = 0
 
class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 20)
 
    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height
 
    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15
 
    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10
 
    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10
 
 
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
 
# Get ready to print
textPrint = TextPrint()
 
button_pressed = 0
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            button_pressed = 1
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            button_pressed = 0
            connection.send(("0 Buttons pressed").encode())

            print("Joystick button released.")
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()
 
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
 
    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()
 
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
 
        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()
 
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))
 
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()
 
        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            if var_speed == 0:
                if i == 2 and axis > -0.1:
                    speed = 0
                    #connection.send(("Zero speed").encode())
                if i == 2 and axis > -0.1 and axis <-0.05:
                    speed = 0
                    #connection.send(("Speed 0").encode())
                if i == 2 and axis <= -0.1 and axis > -0.3:
                    speed = 1
                    #connection.send(("Speed 1").encode())
                if i == 2 and axis <= -0.3 and axis > -0.5:
                    speed = 2
                    #connection.send(("Speed 2").encode())
                if i == 2 and axis <= -0.5 and axis > -0.7:
                    speed = 3
                    #connection.send(("Speed 3").encode())
                if i == 2 and axis <= -0.7 and axis > -0.9:
                    speed = 4
                    #connection.send(("Speed 4").encode())
                if i == 2 and axis <= -0.9 and axis > -1:
                    speed = 5
            if var_speed == 1:
                speed = 3
                
                
                
            if i == 0 and axis >= 0.9 and axis <= 1:
                angle = -4                    
            if i == 0 and axis >= 0.7 and axis < 0.9:
                angle = -3                    
            if i == 0 and axis >= 0.5 and axis < 0.7:
                angle = -2
            if i == 0 and axis >= 0.3 and axis < 0.5:
                angle = -1
            if i == 0 and axis >=0.1 and axis < 0.3:
                angle = 0
            if i == 0 and axis > -0.1 and axis < 0.1:
                angle = 0
            if i == 0 and axis <= -0.1 and axis > -0.3:
                angle = 0
            if i == 0 and axis <= -0.3 and axis > -0.5:
                angle = 1
            if i == 0 and axis <= -0.5 and axis > -0.7:
                angle = 2
            if i == 0 and axis <= -0.7 and axis > -0.9:
                angle = 3
            if i == 0 and axis <= -0.9 and axis >= -1:
                angle = 4
                    
                    
            """
            if i == 0 and axis > 0.1 and axis <-0.05:
                connection.send(("Angle 0").encode())
            if i == 0 and axis <= 0.1 and axis > -0.3:
                connection.send(("Angle 1").encode())
            if i == 0 and axis <= 0.3 and axis > -0.5:
                connection.send(("Angle 2").encode())
            if i == 0 and axis <= 0.5 and axis > -0.7:
                connection.send(("Angle 3").encode())
            if i == 0 and axis <= 0.7 and axis > -0.9:
                connection.send(("Angle 4").encode())
            if i == 0 and axis <= 0.9 and axis > -1:
                connection.send(("Angle 5").encode())
                
            """

        textPrint.unindent()
        connection.send(("Speed = "+str(speed)+" angle = "+str(angle)).encode())

        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()
 
        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
            if i == 0 and button == 1:
                var_speed = 1
            if i == 1 and button == 1:
                var_speed = 0
            if i == 2 and button == 1:
                connection.send(("Button {:>2} value: {}".format('X', button)).encode())
            if i == 3 and button == 1:
                connection.send(("Button {:>2} value: {}".format('Y', button)).encode())
        textPrint.unindent()
 
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()
 
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()
 
        textPrint.unindent()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()