#Use this logic to create the stars and planet 

import matplotlib.pyplot as plt

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Plotting the star at the specified coordinates
        plt.scatter(self.x, self.y, marker='*', color='gold', s=200)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Star class with coordinates (2, 3)
    star_instance = Star(2, 3)

    # Draw the star
    star_instance.draw()

    # Set plot limits and show the plot
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
