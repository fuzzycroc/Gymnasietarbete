import rebound
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Initial conditions for the planet (you can change these values)
initial_planet_x = 0.0
initial_planet_y = 0.513
initial_planet_vx = 0.0
initial_planet_vy = 0.0


# Function to set up the simulation
def setup_simulation(planet_x, planet_y, planet_vx, planet_vy):
    sim = rebound.Simulation()

    # Add binary stars
    m_star = 1.0  # mass of the stars
    d_star = 1.0  # distance between the stars
    
    sim.add(m=m_star, x=-d_star, vy=0.5, hash="star1")
    sim.add(m=m_star, x= d_star, vy=-0.5, hash="star2")

    # Add planet
    m_planet = 0.001  # mass of the planet
    sim.add(m=m_planet, x=planet_x, y=planet_y, vx=planet_vx, vy=planet_vy, hash="planet")

    # Set up simulation parameters
    sim.move_to_com()
    sim.integrator = "ias15"
    sim.dt = 0.02

    return sim

# Function to update the plot in each animation frame
def update(frame, ax, sim):
    sim.integrate(sim.t + 0.1)  # Integrate a small time step
    ax.cla()

    # Plot stars
    ax.scatter(sim.particles["star1"].x, sim.particles["star1"].y, color="red", s=10, label="Star 1")
    ax.scatter(sim.particles["star2"].x, sim.particles["star2"].y, color="blue", s=10, label="Star 2")

    # Plot planet
    ax.scatter(sim.particles["planet"].x, sim.particles["planet"].y, color="green", s=50, label="Planet")


    # Set plot limits and labels
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()


# Set up the initial simulation
simulation = setup_simulation(initial_planet_x, initial_planet_y, initial_planet_vx, initial_planet_vy)

# Create the plot and animation
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, fargs=(ax, simulation), frames=10, interval=50, blit=False)

plt.show()