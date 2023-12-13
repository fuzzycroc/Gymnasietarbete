#Use this logic to create the stars and planet 

import matplotlib.pyplot as plt
import math

class Star:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    Scale = 250 / AU
    Timestep = 3600*24

def __init__(self, x, y, mass):
        self.x = x
        self.y = y, self.mass = mass
		
        
def draw(self):
        # Plotting the star at the specified coordinates
        plt.scatter(self.x, self.y, marker='*', color='gold', s=200)

def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		if other.sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

def update_position(self, planets):
		total_fx = total_fy = 0
		for planet in planets:
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))


star_instance1 = Star(-1, -1)
star_instance2 = Star(1, 1)

x = [0]
y = [0]
plt.scatter(x,y, marker= 'o', s= 1, color = 'red')


    
star_instance1.draw()
star_instance2.draw()

plt.xlim(-12, 12)
plt.ylim(-12, 12)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()