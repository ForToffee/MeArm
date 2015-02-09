import pygame, sys, time, os
import servoblst as servo

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode((400,300))

sc = servo.ServoController()
grip = 1
elbow = 3
shoulder = 4
hip = 5

def reset():
	sc.setAngle(grip, 90)
	sc.setAngle(elbow, 0)
	sc.setAngle(shoulder, 25)
	sc.setAngle(hip, 0)

threshold = 0.5
def handleMovement(servo_id, event_value, inc=2):
	ret = ''
	if event_value > threshold:
		ret = sc.incAngle(servo_id, inc)
	elif event_value < threshold * -1:
		ret = sc.incAngle(servo_id, inc * -1)
	
	if ret <> '':
		print "servo %d = %d degrees" % (servo_id, ret)
		
reset()
interval = 0.1
try:
	run = True
	while run:
		events = pygame.event.get()
		for event in events:

			# Check if one of the joysticks has moved
			if event.type == pygame.JOYAXISMOTION:
				if event.axis == 1:
					handleMovement(elbow, event.value)
				
				if event.axis == 2:
					handleMovement(hip, event.value * -1)

				if event.axis == 3:
					handleMovement(shoulder, event.value * -1)
					
			if event.type == pygame.JOYBUTTONDOWN:
				if event.button == 0:	#select
					run = False
				if event.button == 3:	#start
					reset()
				if event.button == 12:	#triangle
					sc.setAngle(grip, 90)
				if event.button == 14:	#X
					sc.setAngle(grip, 30)
				else:
					print event.button
					
		time.sleep(interval)
except KeyboardInterrupt:
	pass

except Exception as e:
	print e
	pass

reset()
sc.clean_up()
