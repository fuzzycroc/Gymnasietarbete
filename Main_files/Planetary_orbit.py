#imports 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation

time = 1000
for i in range (1000):
    time -= 1

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
    
            

    
         


        
#Creates bodies
Star_1 = Star(100, 0, 20, 20, 0, 10, 'o','red') #this one has x_vel


Binary_Star_2 = Star(-1, 0, 20, 0, 0, 10, 'o', 'black')
planet = Star(40, 40, 4, 0, 0, 14,'*', 'blue')



#draws bodies
Star_1.draw()
Binary_Star_2.draw()
planet.draw()


plt.xlim (-120, 120)
plt.ylim (-120, 120)
plt.show()

