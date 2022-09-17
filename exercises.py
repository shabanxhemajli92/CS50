#Task 1
text=("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
print(text)
#Task2
#Python program to retrive the python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
#task 3
from datetime import datetime
import datetime
now=datetime.datetime.now()
print("current date and time",now)
#task 4
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#Task5
name=input("what is your name? ")
last_name=input("what is your last name? ")
print(last_name,"",name)