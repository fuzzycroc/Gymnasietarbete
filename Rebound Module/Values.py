#File for storing values of planet and plot limits 
import numpy as np

Planet_Mass = 0.001             #Mass of the planet

X_Planet = 0                   
Y_Planet = 12   

Velocity = np.sqrt(2/Y_Planet)  

Vx_Planet = Velocity                               
Vy_Planet = 0.0                      

Time_Step = 100                    #Time_Step of Simulation

Limits = X_Planet + Y_Planet + 2    #Graph limits  