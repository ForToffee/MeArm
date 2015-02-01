#!/usr/bin/env python
from flask import Flask, render_template, Response
import servo

app = Flask(__name__)

grip =servo.ServoController(17)
grip.setAngle(90)

elbow =servo.ServoController(27)
elbow.setAngle(0)

shoulder =servo.ServoController(22)
shoulder.setAngle(25)

hip =servo.ServoController(23)
hip.setAngle(0)


@app.route('/')
def index():
	try:
		return render_template('arm.html')
	except Exception as e:
		print e
		pass
		
				
@app.route("/<direction>")
def move(direction):
	# Choose the direction of the request
	if direction == 'gopen':
		grip.setAngle(45)
        
	elif direction == 'gclose':
		grip.setAngle(90)

	elif direction == 'eup':
		elbow.incAngle(10)

	elif direction == 'edown':
		elbow.incAngle(-19)

	elif direction == 'sback':
		shoulder.incAngle(-10)

	elif direction == 'sfwd':
		shoulder.incAngle(10)

	elif direction == 'hleft':
		hip.incAngle(-10)

	elif direction == 'hright':
		hip.incAngle(10)

	return direction
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
