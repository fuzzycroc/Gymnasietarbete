#This is a siplified version with only the Binary stars included


import matplotlib.pyplot as plt
import numpy as np
import math

G = 6.67408e-11  # Gravitational Constant
Star_mass = 1.989e+30  # Solar mass to kg
Au = 149.6e+9  # AU to m
Main_Stardistance = (2*Au)

Acceleration_Star = (G * Star_mass) / Main_Stardistance**2
Velocity_Star = (math.sqrt(G * Star_mass/Main_Stardistance))

class Star: 
    def __init__(self, x, y, mass, velocity, radius, marker, color):
        self.x = x *Au
        self.y = y *Au
        self.mass = mass 
        self.velocity = velocity
        self.radius = radius 
        self.marker = marker 
        self.color = color 
    
    def draw(self):
        plt.scatter(self.x, self.y, s = self.radius**2, c = self.color, marker = self.marker)


print("Acceleration", Acceleration_Star)
print("velocity", Velocity_Star)