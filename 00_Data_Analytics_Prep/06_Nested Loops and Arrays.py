#### Nested Loops and Arrays ####

#### Basic Nested Loops

exter_vals = [1,2,3]
inter_vals = ["x","y","z"]

for e_vals in exter_vals:
	for i_vals in inter_vals:
		print (e_vals, i_vals)


for i in range(1,7):
	for j in range(1,11):
		print ("%3d" % (i * j), end = " ")

#### Simple Bubble Sort ####

raw_list = [2,4,10,1,8,7,0,1,7,2]

for j in range(len(raw_list)):
	for i in range(len(raw_list)-1-j):	
		
		if raw_list[i] > raw_list[i+1]:	# Is the current value bigger than the next one?
			 raw_list[i], raw_list[i+1] = raw_list[i+1], raw_list[i] # Swap the values


print(raw_list)	

#### Further Bubble Sort ####

# function to check if the list is in order

def in_order(x):
	
	for i in range(len(x)-1):
		if x[i] > x[i+1]:
			return False
			
	return True

# Test call to function
# print(in_order(raw_list))

# bubble sort contain within a while loop

raw_list = [2,4,10,1,8,7,0,1,7,2]

while in_order(raw_list) != True:
	
	for i in range(len(raw_list)-1):
		if raw_list[i] > raw_list[i+1]:	
			 raw_list[i], raw_list[i+1] = raw_list[i+1], raw_list[i]
	
print(raw_list)

# Bubble sort in two for loops

raw_list = [2,4,10,1,8,7,0,1,7,2]

for j in range(len(raw_list)):
	for i in range(len(raw_list)-1-j):
			
		
		if raw_list[i] > raw_list[i+1]:	
			 raw_list[i], raw_list[i+1] = raw_list[i+1], raw_list[i]
		
		if in_order(raw_list) != False:
			break 

print(raw_list)

#### Multi Dimensional Arrays ####

import pylab as pl

# create an array filled with zero
print(pl.zeros(5))

# create array filled with a sequence of values with a non integer step
print(pl.arange(0,2,0.3))

# Create a multi dimension array
print(pl.zeros((3,5)))

# Report on the shape of the array
x = pl.zeros((3,5))
print(x.shape)

# Using nested loops to address the elements of a 2D array
x_array = pl.zeros((3,5))	# (rows, columns)

val = 0

for row in range(3):
	for col in range(5):
		val += 0.1
		x_array[row][col] = val

print(x_array)























