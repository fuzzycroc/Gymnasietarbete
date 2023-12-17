import math

#Class for planet and Sun
class Planet: 
    AU = 149.6e6 * 1000 
    G = 6.67428e-11

    def __init__(self,x,y, radius, marker, color,mass,x_vel, y_vel):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.marker = marker
        self.color = color 
        self.mass = mass 
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.orbit = [] #creates empty list for orbital distance for planet

#Define gravity so that it works with matplotlib
        
#Class for star 
#requirements? x and y coordinates  
class Star: 

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
