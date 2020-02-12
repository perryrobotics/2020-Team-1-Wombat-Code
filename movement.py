#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    

def forward(speed, ticks):
	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
  	KIPR.mav(LMOTOR, speed)
  	KIPR.mav(RMOTOR, speed)
 	while KIPR.gmpc(LMOTOR) < ticks:
		pass
	KIPR.ao()
  	KIPR.msleep(DELAY)

def backward(speed, ticks):
	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
  	KIPR.mav(LMOTOR, -speed)
  	KIPR.mav(RMOTOR, -speed)
 	while KIPR.gmpc(LMOTOR) >-ticks:
		pass
  	KIPR.ao()  
   	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
  	KIPR.msleep(DELAY)
    
def left(speed, ticks):
	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
 	KIPR.mav(LMOTOR, -speed)
 	KIPR.mav(RMOTOR, speed)
  	while KIPR.gmpc(RMOTOR) < ticks:
		pass
	KIPR.ao()
   	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
 	KIPR.msleep(DELAY)
        
def right(speed, ticks):
	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
  	KIPR.mav(LMOTOR, speed)
  	KIPR.mav(RMOTOR, -speed)
 	while KIPR.gmpc(LMOTOR) < ticks:
		pass 
	KIPR.ao()
   	KIPR.cmpc(RMOTOR)
  	KIPR.cmpc(LMOTOR)
  	KIPR.msleep(DELAY)
        
def forward_time(speed, time):
	KIPR.motor(LMOTOR,  speed)
 	KIPR.motor(RMOTOR, speed)
  	KIPR.msleep(time)
 	KIPR.ao()
  	KIPR.msleep(DELAY)

def backward_time(speed, time):
	KIPR.motor(LMOTOR,  -speed)
 	KIPR.motor(RMOTOR, -speed)
  	KIPR.msleep(time)
 	KIPR.ao()
  	KIPR.msleep(DELAY)

        

