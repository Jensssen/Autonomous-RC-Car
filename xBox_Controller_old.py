import pygame
print("loading packages done!")

pygame.init()
print("init pygame done!")

WHITE = (255, 255, 255)
# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
	# No joysticks!
	print("Error, I didn't find any joysticks. Program will be terminated!")
	quit()
else:
	print("Found X-Box controller!!!!")
	# Use joystick #0 and initialize it
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()

#Open Window and set dimensions
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(WHITE)
#Give window a caption
pygame.display.set_caption('Autonomous Car Control')

#Start the game Clock
clock = pygame.time.Clock()

crashed = False

while not crashed:
	
	for event in pygame.event.get():
		horiz_axis_pos = my_joystick.get_axis(0)
		vert_axis_pos = my_joystick.get_axis(1)

		#If the event = QUIT, quit the game
		if event.type == pygame.QUIT:
			crashed = True
		print("X = ",horiz_axis_pos)
		print("Y = ",vert_axis_pos)
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()
