#Use this logic to create the stars and planet 

import matplotlib.pyplot as plt

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Plotting the star at the specified coordinates
        plt.scatter(self.x, self.y, marker='*', color='gold', s=200)


star_instance1 = Star(2, 3)
star_instance2 = Star(0,0)

    
star_instance1.draw()
star_instance2.draw()

plt.xlim(-12, 12)
plt.ylim(-12, 12)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()