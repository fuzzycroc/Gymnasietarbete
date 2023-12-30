import rebound
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Values import Planet_Mass, X_Planet, Y_Planet, Vx_Planet, Vy_Planet, Limits



# Function to set up the simulation
def setup_simulation(planet_x, planet_y, planet_vx, planet_vy):
    sim = rebound.Simulation()

    # Add binary stars
    m_star = 1.0  # mass of the stars
    d_star = 1.0  # distance between the stars
    
    sim.add(m=m_star, x=-d_star, vy=0.5, hash="star1")
    sim.add(m=m_star, x= d_star, vy=-0.5, hash="star2")

    # Add planet
    
    sim.add(m=Planet_Mass, x=X_Planet, y=Y_Planet, vx=Vx_Planet, vy=Vy_Planet, hash="planet")

    # Set up simulation parameters
    sim.move_to_com()
    sim.integrator = "ias15"

    return sim

# Function to update the plot in each animation frame
def update(frame, ax, sim):
    sim.integrate(sim.t + 0.1)  # Integrate a small time step
    ax.cla()

    # Plot stars
    ax.scatter(sim.particles["star1"].x, sim.particles["star1"].y, color="red", s=200, label="Star 1")
    ax.scatter(sim.particles["star2"].x, sim.particles["star2"].y, color="blue", s=200, label="Star 2")

    # Plot planet
    ax.scatter(sim.particles["planet"].x, sim.particles["planet"].y, color="green", s=50, label="Planet")


    # Set plot limits and labels
    ax.set_xlim(-Limits, Limits)
    ax.set_ylim(-Limits, Limits)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()


# Set up the initial simulation
simulation = setup_simulation(X_Planet, Y_Planet, Vx_Planet, Vy_Planet)

# Create the plot and animation
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, fargs=(ax, simulation), frames=10, interval=50, blit=False)

plt.show()