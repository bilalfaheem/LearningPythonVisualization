import numpy as np
import matplotlib.pyplot as plt
x = np.array([3,4,5])
y = np.array([4,1,8])
plt.plot(x,y)
plt.show()
#line chart
points = np.array([2,6,7,3])
#plt.plot(points)
#plt.plot(points,linestyle = "dotted")
plt.plot(points,linestyle = "dashed")
plt.show()

#bar chart
# one categorical and numerical values
x = np.array(["X","D","W","T"])
y = np.array([34,32,67,12])
plt.bar(x,y)
plt.show()

#scatter plot
x1 = np.array([32,11,56,76])
y1 = np.array([3,1,5,7])
plt.scatter(x1,y1)
plt.show()

#pie chart
p = np.array([32,12,54,23])
plt.pie(p)
plt.show()

#histogram
h1 = np.random.normal(170,10,2500)
h2 = np.array([23,12,34,54])
plt.hist(h1)
plt.show()