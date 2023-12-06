#import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation
 
#Gives both stars x and y coordinates
x =[2,-2]
y = [2,-2]

#Creates star
plt.scatter(x, y, label ="test", color= "red", marker= "*", s=30)

#Plots the x and y axis 
plt.xlabel('X-coordinates[Au]')
plt.ylabel('Y-coordinates[Au]')

#Creates limits of graph
plt.xlim (-20, 20)
plt.ylim (-20, 20)

plt.show()

