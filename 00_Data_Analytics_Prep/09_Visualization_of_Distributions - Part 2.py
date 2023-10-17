#### Excercise 2 - Diagnosing Liver Disease with functions ####

import numpy as np
import matplotlib.pylab as plt

#### Implement a function to compare any value to having the disease 

# fn graph_corelation: takes the value of the column and shows two histograms

def graph_corelation(column_ex):
	
	# get the data
	data = np.loadtxt(open("files/liver_data.txt","rb"), delimiter=",")
	
	# Extract the well people and ill people
	well_people = data[data[:,6]==1, column_ex]
	ill_people = data[data[:,6]==2, column_ex]
	
	# configure the minimum of the graph
	if min(well_people) < min(ill_people):
		minimum = min(well_people)
	else:
		minimum = min(ill_people)
	
	# configure the maximum of the graph
	if max(well_people) > max(ill_people):
		maximum = max(well_people)
	else:
		maximum = max(ill_people)
	
	# configure the spacing of the hist bins
	
	# Plot the data
	plt.subplot(2,1,1)
	plt.hist(well_people, bins=np.linspace(minimum, maximum, 22))
	
	plt.subplot(2,1,2)
	plt.hist(ill_people, bins=np.linspace(minimum, maximum, 22))
	
	plt.show()

#### Corelation between two factors with scatter graphs

def scatter_corelation(x_var, y_var):
	
	# Read the data file
	data = np.loadtxt(open("files/liver_data.txt","rb"), delimiter=",")
	
	# extract the required data for the x_var
	well_x = data[data[:,6]==1, x_var]
	ill_x = data[data[:,6]==2, x_var]
	
	# extract the required data for the y_var
	well_y = data[data[:,6]==1, y_var]
	ill_y = data[data[:,6]==2, y_var]
	
	# Plotting the scatter graph
	plt.scatter(ill_x, ill_y, s=20, c='r', marker='o')
	plt.scatter(well_x, well_y, s=20, c='g', marker='x')
	
#### fn: to print the 36 possible scatter plots

def all_correlations():
	
	pos_count = 1
	
	for i in range(6):
		for j in range(6):
			
			# plot the relevent scatter graph
			plt.subplot(6,6,pos_count)
			scatter_corelation(i,j)
			
			pos_count += 1
			
	# show the graphs
	plt.show()
	

# Function Tests
all_correlations()
