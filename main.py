#!/usr/bin/python
import os, sys
import ctypes
from constants import *
from sensors import *
from movement import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

KIPR.enable_servos()

#start position
KIPR.set_servo_position(ARM_SERVO, 1400)
KIPR.set_servo_position(ELBOW_SERVO, 2000)
claw_fullopen(50)
tail_up(50)
print("Press  a to start, sucker!!")
while KIPR.a_button() == 0:
	pass
KIPR.msleep(2000) 
#====================================================================================================
#Go Play Botball!!
        
forward(900, 2500)
claw_halfopen(50)
arm_back(50)
backward(900, 3000)
claw_fullopen(50)
right(900,300)
backward(900,1450)
left(900,250)
backward(900,700)
tail_down(50)
forward(1000, 2500)
left(1000, 1400)
backward(1000,4500)
tail_up(50)
tail_middle(50)
right(1000, 500)
left(1000, 500)
move_to_black(1000, LINE_PORT_LEFT)
forward(1000,2000)
move_to_black(1000, LINE_PORT_LEFT)
right(1000,100)
forward(1000,2000)
backward(1000,1200)
left(1000,900)

forward(1000,4600)  #hit the pipe
backward(1000,400)

        
        
        
left(1000,900)     #heading up the ramp
backward(500, 1000)
forward(1400,2000)
#line_follow_bump(1000)
KIPR.mav(LMOTOR,1000)
KIPR.mav(RMOTOR, 1000)
while KIPR.digital( BUMP_PORT) == 0:
	pass
KIPR.ao()
backward(1000,400)
left(1000, 800)
backward(1000, 2000)
line_follow_dist(1000, 5000)
claw_closed(50)
#IN FRONT OF MINE
forward(1000,1550)        
#over mine
move_servo_slow( ARM_SERVO, 500, 10)
move_servo_slow(ELBOW_SERVO, 1300, 10)
        
        
        
        
        
        
        
        
        
        