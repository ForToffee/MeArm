#!/usr/bin/env python
import servo

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

	

while True:
	servo = raw_input('Servo (g/e/s/h): ')
	action = raw_input('Action: ')
	
	move(servo,action)
	