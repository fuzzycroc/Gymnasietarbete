import rebound
import matplotlib.pyplot as plt

Planet_Mass = 0.001
X_Planet = 0.1
Y_Planet = 0.0
Vx_Planet = 0.3
Vy_Planet = 1.6

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
    

    return sim

# Function to update the plot in each animation frame
def update(frame, ax, sim, orbits):
    sim.integrate(sim.t + 0.1)  # Integrate a small time step
    ax.cla()

    # Plot stars
    ax.scatter(sim.particles["star1"].x, sim.particles["star1"].y, color="red", s=100, label="Star 1")
    ax.scatter(sim.particles["star2"].x, sim.particles["star2"].y, color="blue", s=100, label="Star 2")

    ax.scatter(sim.particles["Planet"].x, sim.particles["Planet"].y, color="black", s=50, label="Planet")

    # Plot orbits for stars
    for i in range(2):
        orbits[i].append((sim.particles[i].x, sim.particles[i].y))
        orbit_x, orbit_y = zip(*orbits[i])
        ax.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")

    # Plot orbit for the planet
    planet_orbit = sim.particles["Planet"].sample_orbit()
    orbit_x, orbit_y, _ = zip(*planet_orbit)  # Unpack three values instead of two
    ax.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")


    # Set plot limits and labels
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()

# Set up the initial simulation
simulation = setup_simulation()

# Create the plot
fig, ax = plt.subplots()

# Initialize orbits
orbits = [[] for _ in range(2)]

# Update the plot without animation
for _ in range(200):
    update(_, ax, simulation, orbits)

plt.show()