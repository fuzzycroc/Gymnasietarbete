import rebound
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a simulation
sim = rebound.Simulation()

# Add a Sun-like star at the center
sim.add(m=1.0)

# Add a planet orbiting the star    
sim.add(a=1.0, e=0.1, m=1e-6)

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], label='Planet Orbit')
scatter_initial = ax.scatter([], [], color='red', marker='o', label='Initial Position')
scatter_final = ax.scatter([], [], color='green', marker='o', label='Final Position')

# Set plot labels and title
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_title('Simulation of Planet Orbit')
ax.legend()

# Function to initialize the plot
def init():
    ax.set_xlim(-1.5, 1.5)  # Set fixed X-axis limits
    ax.set_ylim(-1.5, 1.5)  # Set fixed Y-axis limits

    line.set_data([], [])
    scatter_initial.set_offsets([])
    scatter_final.set_offsets([])
    return line, scatter_initial, scatter_final

# Function to update the plot for each animation frame
def update(frame):
    sim.integrate(frame)
    x = [sim.particles[i].x for i in range(sim.N)]
    y = [sim.particles[i].y for i in range(sim.N)]

    line.set_data(x, y)
    scatter_initial.set_offsets([[x[0], y[0]]])
    scatter_final.set_offsets([[x[-1], y[-1]]])

    return line, scatter_initial, scatter_final

# Animate the plot
animation = FuncAnimation(fig, update, frames=range(0, 101, 1), init_func=init, blit=True)

# Show the animation
plt.show()
