#import libraries 
import matplotlib.pyplot as plt 

#Gives both stars x and y coordinates
x =[2,-2]
y = [2,-2]

#Creates star
plt.scatter(x, y, label ="test", color= "red", marker= "*", s=30)

#Plots the x and y axis 
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Creates limits of graph
plt.xlim (-100, 100)
plt.ylim (-100, 100)

plt.show()

