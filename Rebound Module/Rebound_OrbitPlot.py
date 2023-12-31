import rebound
import matplotlib.pyplot as plt
import numpy as np
import os
from Values import Planet_Mass, X_Planet, Y_Planet, Vx_Planet, Vy_Planet, Limits, Time_Step
from scipy.signal import find_peaks

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

# Function to detect peaks in the distance graph
def detect_peaks(distances):
    peaks, _ = find_peaks(distances)
    return peaks

# Function to update the plot in each animation frame
def update(frame, ax1, ax2, sim, orbits, distances):
    sim.integrate(sim.t + 0.1)  # Integrate a small time step
    ax1.cla()
    ax2.cla()

    # Plot stars and orbits
    ax1.scatter(sim.particles["star1"].x, sim.particles["star1"].y, color="red", s=100, label="Star 1")
    ax1.scatter(sim.particles["star2"].x, sim.particles["star2"].y, color="blue", s=100, label="Star 2")
    ax1.scatter(sim.particles["Planet"].x, sim.particles["Planet"].y, color="black", s=50, label="Planet")

    for i in range(3):
        orbits[i].append((sim.particles[i].x, sim.particles[i].y))
        orbit_x, orbit_y = zip(*orbits[i])
        ax1.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")

    planet_orbit = sim.particles["Planet"].sample_orbit()
    orbit_x, orbit_y, _ = zip(*planet_orbit)
    ax1.plot(orbit_x, orbit_y, linestyle="--", alpha=0.5, color="gray")

    ax1.set_xlim(-Limits, Limits)
    ax1.set_ylim(-Limits, Limits)
    ax1.set_xlabel("X Coordinate(AU)")
    ax1.set_ylabel("Y Coordinate(AU)")
    ax1.legend()

    # Plot distance of the planet from the center as a function of time
    distances.append(np.linalg.norm([sim.particles["Planet"].x, sim.particles["Planet"].y]))
    ax2.plot(np.arange(len(distances)), distances, color="green", label="Distance from Center")

    ax2.set_xlabel("Time Step")
    ax2.set_ylabel("Distance from Center(AU)")
    ax2.set_ylim(min(distances) - 0.1, max(distances) + 0.1)  # Set y-axis limits to include min and max values
    ax2.legend()

    # Detect peaks in the distance graph
    peaks = detect_peaks(distances)

    # Plot the detected peaks on the distance graph
    ax2.plot(peaks, np.array(distances)[peaks], "rx", label="Peaks")
    ax2.legend()

    # Add text annotations for all peak values
    for peak in peaks:
        ax2.text(peak, distances[peak], f"{distances[peak]:.2f} AU", ha='center', va='bottom', color='purple')

# Set up the initial simulation
simulation = setup_simulation()

# Create the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Initialize orbits and distances
orbits = [[] for _ in range(3)]
distances = []

# Update the plot without animation
for step in range(Time_Step):
    update(step, ax1, ax2, simulation, orbits, distances)


# Set titles for each subplot
ax1.set_title("Orbits and Trajectory")
ax2.set_title("Distance from Center Over Time")



save_directory = r"C:\Users\Perie\Downloads\Gymnasiet_Arbete_Results"
filename = os.path.join(save_directory, f"Planetary_Orbit{Y_Planet, Time_Step}.png")
plt.savefig(filename)

plt.show()
