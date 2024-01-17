The main purpose of this project is to create a simulation of a circumbinary star system
  For the simplification of this simulation the following assumptions are made
      1) The stars orbit are of same mass and orbit each other at the same distance 
      2) The orbit of stars have an eccentricity of 0 
      3) The planet has a mass of near zero and can have a prograde or retrograde motion

These assumptions make it possible to evalute the orbit of a circumbinary planet

The Rebound module is used to return the values of the objects in the simulatio. 
There are several different simulations some which work and most are incomplete. 
The main simulations are inculded in the folder called 'Rebound Module'

  Rebound_Animation.py includes animations for the systems 
 
  Rebound_OrbitPlot.py includes fixed plots and graphs for the systems 

  Rebound_Refernce.py was my personal refernace sheet for understanding how Rebound works
 
  Values.py includes all the values that are used for the entire simulation, 
            which is used in both the animation and the orbitplot files. 
            If you change any value in the values files these are automatically changed in the other files. 
