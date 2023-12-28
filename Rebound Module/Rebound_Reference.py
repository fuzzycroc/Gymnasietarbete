import rebound #import rebound library 
import matplotlib.pyplot as plt


sim = rebound.Simulation() #Creates simulations 
sim.add(m=1) #sim.add adds simulation m=1 Mass is one solar Mass 
sim.add(m=1e-3, x=1,vy=1) #x coordinates vy is velocity in y axis
sim.integrate(10000) #10 000 time steps 

sim.status() #Returns status of object

com = sim.com() #Calculates the center of mass

sim.move_to_com() #move simulation to center of mass

energy = sim.energy() #calculates total energy (kinetic plus potential energy)

Lx, Ly, Lz = sim.angular_momentum() #Calculates the angular momentum of a simulation

#Orbital elements 

sim = rebound.Simulation() #creates new simulation

sim.add (m=1, x =2)
sim.add (a=1) #Object with semi-major axis of 1 (mass is assumed to be 0)
sim.add(a=2, e=0.9) #adds eccentricity

#maximum 6 orbital elements
sim.add(a =3, e = 0.3, f = 0.1, omega =0.4, inc =0.1, Omega = 0.3) 
#f (phase of the orbit), omega (orientation of the periostron), inc (inclination of the system), Omega (orientation of the ascending node)
#error message if to many orbital 

rebound.OrbitPlot(sim)

#Max and min size of graph 
#Should be added after rebound.OrbitPlot
plt.xlim (-10,10)
plt.ylim (-10,10)

#Plots the orbit in matplotlib
plt.show()