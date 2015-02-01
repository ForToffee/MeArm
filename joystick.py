import pygame, sys, time, os
import servo

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
#pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode((400,300))
#pygame.display.set_caption('Hello World')
clock = pygame.time.Clock()

grip =servo.ServoController(17)
grip.setAngle(90)

elbow =servo.ServoController(27)
elbow.setAngle(0)

shoulder =servo.ServoController(22)
shoulder.setAngle(25)

hip =servo.ServoController(23)
hip.setAngle(0)


def move(servo, action):
	# Choose the direction of the request
	if servo == 'g':
		if action == 'o':
			grip.setAngle(45)
		elif action == 'c':
			grip.setAngle(90)
	
	elif servo == 'e':
		elbow.setAngle(int(action))

	elif servo == 's':
		shoulder.setAngle(int(action))

	elif servo == 'h':
		hip.setAngle(int(action))

	
interval = 0.1
while True:
	clock.tick(60)
	pygame.event.pump()
           	 
    	# other event tests, but polling seems to work better in main loop
	if joystick.get_button(12) == True:
		shoulder.incAngle(1)
	elif joystick.get_button(14) == True:
		shoulder.incAngle(-1)

		#if event.type == pygame.JOYBUTTONUP:
		#	print("joy button up")
		#if event.type == pygame.JOYBALLMOTION:
		#	print("joy ball motion")
    	# axis motion is movement of controller
    	# dominates events when used
		#if event.type == pygame.JOYAXISMOTION:
		#	if event.axis <= 4 and event.value <> 0:
		#		print("%1 %2 joy axis motion", event.axis, event.value)

	# pygame.display.update()
	#time.sleep(interval)

