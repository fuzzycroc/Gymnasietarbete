import rebound
import matplotlib.pyplot as plt
from Values import Planet_Mass, X_Planet, Y_Planet, Vx_Planet, Vy_Planet, Limits


# Function to set up the simulation
def setup_simulation():
    sim = rebound.Simulation()

    # Add binary stars
    m_star = 1.0  # mass of the stars
    d_star = 1.0  # distance between the stars

    sim.add(m=m_star, x=-d_star, vy=0.5, hash="star1")
    sim.add(m=m_star, x=d_star, vy=-0.5, hash="star2")

    sim.add(m=Planet_Mass, x=X_Planet, y=Y_Planet, vx=Vx_Planet, vy=Vy_Planet, hash="Planet")  # Add Planet

    # Set up simulation parameters
    sim.move_to_com()
    sim.integrator = "ias15"
    sim.dt = 0.1

    return sim

# Function to update the plot in each animation frame
def update(frame, ax, sim, orbits):
    sim.integrate(sim.t + 0.1)  # Integrate a small time step
    ax.cla()

    # Plot stars
    ax.scatter(sim.particles["star1"].x, sim.particles["star1"].y, color="red", s=100, label="Star 1")
    ax.scatter(sim.particles["star2"].x, sim.particles["star2"].y, color="blue", s=100, label="Star 2")

    ax.scatter(sim.particles["Planet"].x, sim.particles["Planet"].y, color="black", s=50, label="Planet")

    plt.scatter(x=X_Planet, y=Y_Planet, marker= "*", s=40, color = "green", label = "Starting Position" )

    # Plot orbits for stars
    for i in range(3):
        orbits[i].append((sim.particles[i].x, sim.particles[i].y))
        orbit_x, orbit_y = zip(*orbits[i])
        ax.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")

    # Plot orbit for the planet
    planet_orbit = sim.particles["Planet"].sample_orbit()
    orbit_x, orbit_y, _ = zip(*planet_orbit)  # Unpack three values instead of two
    ax.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")


    # Set plot limits and labels
    ax.set_xlim(-Limits, Limits)
    ax.set_ylim(-Limits, Limits)
    ax.set_xlabel("X Coordinate(AU)")
    ax.set_ylabel("Y Coordinate(AU)")
    ax.legend()

# Set up the initial simulation
simulation = setup_simulation()

# Create the plot
fig, ax = plt.subplots()

# Initialize orbits
orbits = [[] for _ in range(3)]

# Update the plot without animation
for _ in range(1000):
    update(_, ax, simulation, orbits)

plt.show()