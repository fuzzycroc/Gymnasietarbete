#import libraries 
import matplotlib.pyplot as plt 

#Gives the star a x and y coordinates
x =[0]
y = [0]

#Creates star
plt.scatter(x, y, label ="test", color= "red", marker= "*", s=30)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

