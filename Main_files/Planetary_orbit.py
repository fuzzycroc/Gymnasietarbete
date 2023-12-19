#imports 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation

#Timer trail for measuring orbital periods of the binary stars STATUS: Non-functional
time = 1000

#Class for the Star and Planet 
class Star: 

    #bodies class
    def __init__(self, x, y, mass, x_vel, y_vel,  radius, marker, color):
        self.x = x 
        self.y = y
        self.mass = mass 
        self.x_vel = x_vel 
        self.y_vel = y_vel
        self.radius = radius 
        self.marker = marker 
        self.color = color 

    #draw method
    def draw(self):
        plt.scatter(self.x, self.y, s = self.radius**2, c= self.color, marker = self.marker)
    
    def attraction(self):
        G = 6.67408e-11 #N-m2/kg2
        Au = 1,496e+11 #Au to m
   
    #Issue no.1: Gravitational force defines the attraction between two bodies. 
    #This leads to a certain acceleration that is experienced by both the objects 
        
    #Question 1: As far as I have understood python can only uncderstand x and y position and not acceleration
    #How do I translate Acceleration into x and y velocity.
    #But at the same time make it so that there is x and y velocity of the planet and the stars
        # I thought of using Odient from Scipy.intergrate.odient to solve it.
        # But I have no idea how it works :(

    #Question 2: How do I use the veolcity to give the bodies new x and y positions?
            
    #Question 3: How do I draw the orbits? This part is very important for analysing data for my project 
        #I only know how to update the positons but not how to draw a line from the last position to the new one
    
    #Question 4: Is it possible to get graphs or just data on min and max values (Perihilion and Aphelion) of the planets orbit?

    #Question 5: Is it possible to animate the simulation?
        # I thought of using Funanimation to do this. 
        # But I have only grasped the basics 
        # This part is optional but it looks really cool :)
    
    #Issue no.2: How on earth do I make the x and y coordinates in AU (Astronomical Units)!!!
        



        
#Creates bodies
Star_1 = Star(100, 0, 20, 20, 0, 10, 'o','red') #this one has x_vel


Binary_Star_2 = Star(-1, 0, 20, 0, 0, 10, 'o', 'black')
planet = Star(40, 40, 4, 0, 0, 14,'*', 'blue')



#draws bodies
Star_1.draw()
Binary_Star_2.draw()
planet.draw()

#Creats limits of the graph
plt.xlim (-120, 120)
plt.ylim (-120, 120)
plt.show()

