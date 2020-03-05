from matplotlib import pyplot as plt
import numpy as np

# make arrays of numbers





########################################################
# Repeatability

# make random data as a placeholder for actual data
n = 20
x = np.random.normal(0,1,n)
# # make x
# # make y array
y = np.random.normal(0,1,n)
xmin = np.min(x)
xmax = np.max(x)
ymin = np.min(y)
ymax = np.max(y)

print(xmin)
print(xmax)
print(ymin)
print(ymax)

# plot the points in a scatterplot
plt.scatter(x,y, label='location of Probe')
plt.xlabel( 'meters(x)')
plt.ylabel('meters(y)')
plt.title('Accuracy and precision of CB')
# show plot
plt.show()

r = np.sqrt((ymax-ymin)**2+(xmax-xmin)**2)/2
fig, ax = plt.subplots()
ax.set(xlim=(-5,5), ylim = (-5,5))
a_circle = plt.Circle((0,0), r)
ax.add_artist(a_circle)
plt.show()

# find lowest x-value (lowest value in x array)
# find lowest y-value
# find highest x and y values
# find distance between highest and lowest x
# "                                      " y

# Find radius of circle using half of the longest side length
# # Determine longest of x distance or y distance
# # Take half of the longest length
# print value for the radius
