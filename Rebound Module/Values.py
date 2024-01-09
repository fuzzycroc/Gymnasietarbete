#File for storing values of planet and plot limits 
import numpy as np

Planet_Mass = 1e-30          #Mass of the planet

X_Planet = 2                 
Y_Planet = 0   

Velocity = np.sqrt(2/X_Planet)  

Vx_Planet = 0.0                        
Vy_Planet = Velocity             

Time_Step = 1500                    #Time_Step of Simulation

Limits = X_Planet + Y_Planet + 2    #Graph limits  