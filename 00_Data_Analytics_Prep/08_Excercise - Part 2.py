# Excercise 4

import pylab as pyl 

# Graphing the distance between two asteroids

# fn to calculate the raw distance between two points
def distance_calc(x1,y1,x2,y2):
	return pyl.sqrt((x1-x2)**2 + (y1-y2)**2)

# fn asteroid_path: takes the initial conditions and returns a double array of its path
def asteroid_path(initial_x,initial_y,initial_vx,initial_vy,time_hrs):
	
	
	# Create the array for the results
	asteroid_path_array = []
	
	# For each iteration calculate the new position of the asteroid after 1 hour
	for i in range(time_hrs+1):
		asteroid_path_array.append([initial_x + initial_vx * i, initial_y + initial_vy * i])
		
	return asteroid_path_array

# fn asteroid_distance: takes two arrays of positions and returns the distance between the two arrays for each element 
def asteroid_distance (asteroid_1, asteroid_2):
	
	distance_array = []
	
	# Cycle through each element for both arrays
	for i in range(len(asteroid_1)):
		
		x1,y1 = asteroid_1[i]
		x2,y2 = asteroid_2[i]
		distance_array.append(distance_calc(x1,y1,x2,y2))
		
	return distance_array
		


# fn tests
asteroid_alpha = asteroid_path(150.4, 200.5, 4.9, -7.1, 50)
asteroid_beta = asteroid_path(122.6, 64.0, -5.2, -2.95, 50)
plot_data = asteroid_distance(asteroid_alpha, asteroid_beta)

pyl.plot(plot_data)
pyl.show()
