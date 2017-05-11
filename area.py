#This program calculates the area of a circle or a triangle

from math import *
import time
from datetime import datetime

now=datetime.now()

print "The calculator is starting up"

print "%s-%s-%s %02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
  
time.sleep(2)

option=raw_input("What is the area you want to find?  C for Circle, T for Triangle \n").upper()

if(option=="C"):
  rad=float(raw_input("Enter the radius of the circle: "))
  unit=raw_input("What is the unit measure: ")
  area_circle=pi*rad*rad
  print "The pie is baking..."
  time.sleep(2)
  print "The area of the circle is "+ str(round(area_circle,2)) + " " + str(unit)
elif option=="T":
  ht=float(raw_input("Enter the height of the triangle: "))
  base=float(raw_input("Enter the base of the triangle: "))
  unit=raw_input("What is the unit measure: ")
  area_tri=(base*ht)/2
  print "Uni Bi Tri..."
  time.sleep(2)
  print "The area of traingle is "+ str(round(area_tri,2)) + " " + str(unit)
else:
  print "Please enter a valid value"
  exit()
    
    

  
