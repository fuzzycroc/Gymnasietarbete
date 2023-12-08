import math

#Class for planet and Sun
class Planet: 
    AU = 149.6e6 * 1000 
    G = 6.67428e-11

    def __init__(self,x,y, radius,color,mass,x_vel, y_vel):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.color = color 
        self.mass = mass 
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.orbit = [] #creates empty list for orbital distance for planet

#Force of gravitational attraction 

def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		
		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y