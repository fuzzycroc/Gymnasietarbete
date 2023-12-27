#File for testing animation of matplotlib animation

import scipy as sci
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 
import scipy.integrate

#Idea Use the numerical values to return x and y values and input into a 2d simulation 

#Gravitational Constant
G=6.67408e-11

#Reference Quantites
Star_mass = 1.989e+30  # Solar mass to kg
Au = 149.6e+9  # AU to m
Velocity_Star = 30000 #m/s
Time_scale = 365*24*60*60 #years to seconds


#Net Constants?
Equation_1 = G*Time_scale*Star_mass/(Au**2*Velocity_Star)
Equation_2 = Velocity_Star*Time_scale/Au



#Define masses
Mass_1 = 1
Mass_2 = 1

#Define initial position vectors 
Star_Pos_1 = [-1,0]
Star_Pos_2 = [1,0]

#Convery pos vectors to arrays 
#What does this mean?
Star_Pos_1 = np.array(Star_Pos_1)
Star_Pos_2 = np.array(Star_Pos_2)


#Fincd Centre of Mass 
Centre_of_Mass = (Mass_1 * Star_Pos_1 + Mass_2 * Star_Pos_2)/(Mass_1 + Mass_2)

#Define initial Velocities
Velocity_1 = [0.02,0.02]
Velocity_2 = [-0.05,0]

#Convery velocity vectors to arrays 
Velocity_1 = np.array(Velocity_1)
Velocity_2 = np.array(Velocity_2)

#Find velocity of Centre of Mass 
V_Common = (Mass_1 * Velocity_1 + Mass_2 * Velocity_2)/(Mass_1 + Mass_2)

#Define Three Body Equations 

def ThreeBodyEquations(w,Time_scale,G,Mass_1,Mass_2):
    #Unpack all the variables from the array "w"
    Star_Pos_1 = w[:2]
    Star_Pos_2 = w[2:4]
    Velocity_1 = w[4:6]
    Velocity_2 = w[6:8]

    #Find out the distance between the two bodies 
    Distance_1_2 = sci.linalg.norm(Star_Pos_1-Star_Pos_2)
    Distance_2_1 = sci.linalg.norm(Star_Pos_2-Star_Pos_1)

    #Define the derivatives according to th equations 
    Derivative_Velocity_1 = Equation_1 * Mass_2 * (Star_Pos_2-Star_Pos_1)/Distance_1_2 ** 3
    Derivative_Velocity_2 = Equation_1 * Mass_1 * (Star_Pos_1-Star_Pos_2)/Distance_2_1 ** 3
    Derrivative_Position_1 = Equation_2 * Velocity_1
    Derrivative_Position_2 = Equation_2 * Velocity_2 

    #Package the derivativs into one finar size-18 array 
    Distance_1_2_Derives = np.concatenate((Derrivative_Position_1,Derrivative_Position_2))
    Velocity_1_2_Derives = np.concatenate((Derivative_Velocity_1, Derivative_Velocity_2))
    Main_derives = np.concatenate ((Distance_1_2_Derives, Velocity_1_2_Derives))
    return Main_derives

#Package Inital parameters 
init_parameters = np.array([Star_Pos_1, Star_Pos_2, Velocity_1, Velocity_2])
init_parameters = init_parameters.flatten()
Time_span = np.linspace(0,20,1000) #Time span is 20 orbital years and 1000 points 

#Run the ODE Solver
Three_body_solver = sci.integrate.odeint(ThreeBodyEquations, init_parameters, Time_span, args=(G, Mass_1, Mass_2))

#Store the position solutions into three distinct arrays 
Star_Pos_1_Solution = Three_body_solver[:, :2]
Star_Pos_2_Solution = Three_body_solver[:, 2:5]

#Make the figure
plt.figure(figsize=(10,8))


#create new arrays for animation, this gives you the flexibility
#to reduce the number of points in the animation if it becoms slow
#currently set to select every 4th point
Star_Pos_1_Solution_Animation = Star_Pos_1_Solution[::1,:].copy()
Star_Pos_2_Solution_Animation = Star_Pos_2_Solution[::1,:].copy()

#Set initial marker for planets, that is, blue, red circles at the initial positions 
Head_1 =[ax.scatter(Star_Pos_1_Solution_Animation)]