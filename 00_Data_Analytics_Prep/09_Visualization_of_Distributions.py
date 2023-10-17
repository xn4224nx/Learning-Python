#### Excercise 1 - Diagnosing Liver Disease ####

import numpy as np
import matplotlib.pylab as plt

# Get the data and put it in a matrix
data = np.loadtxt(open("files/liver_data.txt","rb"), delimiter=",")

# Extract a column from the data
num_drinks = data[:,5]		# Extracts the 6th column from the matrix

# calculate the average of the data set
print(np.mean(num_drinks))

# Plot the data

# bins defines the groups of the histograms
# linspace creates a sequence of evenly spaced values between the two values

plt.hist(num_drinks, bins=np.linspace(-0.5,20.5,22))
plt.xlim([-0.5,20.5])		# Changes the axis of the graph
plt.show()

#### Using the class label

# prints a vector with T or F if the value in the column is equal to 1
# print(data[:,6]==1)

# We can extract the rows when the 7th value == 1
well_people = data[:,6]==1

# Extracts the column 6 data for when column 7 == 1
well_drinkers = data[data[:,6]==1, 5]

# Extracts the column 6 data for when column 7 == 2
ill_drinkers = data[data[:,6]==2, 5]

# Comparing the ill and well drinkers

plt.subplot(2,1,1)
plt.hist(well_drinkers, bins=np.linspace(-0.5, 20.5, 22))
plt.xlim(-0.5,20.5);
plt.subplot(2,1,2)
plt.hist(ill_drinkers, bins=np.linspace(-0.5, 20.5, 22))
plt.xlim(-0.5,20.5);
plt.show()
