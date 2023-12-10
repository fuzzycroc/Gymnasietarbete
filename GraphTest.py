#import libraries 
import matplotlib.pyplot as plt 

#Gives the star a x and y coordinates
x =[0]
y = [0]

#Creates star
plt.scatter(x, y, color= "red", marker= "o", s=30)
#plt.scatter plots a scatter plt 
#x,y are coordinates which have been defined earlier
#color is color 
#marker determins which sign is shown on the chart
#the markers that i will be using are "o" for the planet and "*" for the star



plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

