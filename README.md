# MeArm
RaspberryPi &amp; MeArm tinkerings

Blog post describing the goings on here can be found at http://fortoffee.org.uk/2015/02/me-arm-and-me-raspberry-pi/

arm.py
------
This uses Flask to run a simple web interface to control the servos 

arm_cmd.py
----------
Simple command line interface to set the position of a specific servo

servo.py
--------
A class to control the servos using RPIO.GPIO, used by arm.py and arm_cmd.py

joystick.py
-----------
Uses a PS3 controller to define the servo positions

servoblst.py
---------------
A class to control the servos using ServoBlaster, used by joystick.py


#Requirements

Flask - sudo pip install flask

RPIO - sudo pip install rpio 

ServoBlaster - https://github.com/richardghirst/PiBits/tree/master/ServoBlaster