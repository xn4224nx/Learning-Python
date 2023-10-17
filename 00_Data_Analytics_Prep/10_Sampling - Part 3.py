#### Timing Code ####

import timeit
import numpy as np
from functools import partial
import math


def to_time(items):
	for i in range(len(items)):
		items[i] += 1.5
	

test_items = [1, 2, 3] * 100
times = timeit.Timer(partial(to_time, test_items)).repeat(3, 1000)
time_taken = min(times) / 1000

print("%9.9f" % time_taken)


#### Creating efficient algorithms ####

# Create an algothithm that determines if A x B ends in a 7
# From numbers 1 -> 1000, count the total no.

# Iteration 1

def num_end_1(N):
	
	count = 0
	
	# go through the multiples of 1 -> 1000
	
	for i in range(1,N+1):
		
		for j in range(i,N+1):
			
			test_num = i * j
			
			if test_num % 10 == 7:
				#print("The number %4i has a final digit 7:" % (test_num))
				print("%4i x %4i = %4i" % (i,j,test_num))
				count += 1
	
	return count

# Iteration 2
def num_end_2(N):
	
	count = 0
	
	# go through the multiples of 1 -> 1000
	
	for i in range(1,N+1):
		
		for j in range(i,N+1):
			
			
			if (i * j) % 10 == 7:

				count += 1

	return count

num_end_1(31)

# Generate 1mn random numbers in the range 0 to 1
# then find the smallest and largest difference between a pair of adjacent numbers in the list

# iteration 1

def pair_matching(N):
	
	# generate the rand no. in an array
	num_array = np.random.rand(N,1)
	#print(num_array)
	
	# var's to store the min and mix difference between adj numbers
	max_diff = 0.0
	min_diff = 1.0
	
	# go through the list and test the difference between numbers
	for i in range(1, len(num_array) - 1):
		
		# for each number test the number before and after it
		
		# testing the previous number
		if math.fabs(num_array[i] - num_array[i-1]) > max_diff:
			max_diff = math.fabs(num_array[i] - num_array[i-1])
			
		elif math.fabs(num_array[i] - num_array[i-1]) < min_diff:
			min_diff = math.fabs(num_array[i] - num_array[i-1])
		
		# testing the next number
		if math.fabs(num_array[i] - num_array[i+1]) > max_diff:
			max_diff = math.fabs(num_array[i] - num_array[i+1])
			
		elif math.fabs(num_array[i] - num_array[i+1]) < min_diff:
			min_diff = math.fabs(num_array[i] - num_array[i+1])

	# print results
	print(num_array)
	print("The max dif: %4f The min dif: %4f" % (max_diff, min_diff))

pair_matching(10)


# iteration 2
def pair_matching_2(N):
	
	# generate the rand no. in an array
	num_array = np.random.rand(N,1)
	
	# var's to store the min and mix difference between adj numbers
	max_diff = 0.0
	min_diff = 1.0
	return max_diff, min_diff



# Find the integers A and B in the range 1 to 1000 for which A/B lies closest to pi/4.

# iteration 1
def closest_to(target,N):
	
	# go through the multiples of 1 -> 1000
	
	diff = 10000.
	
	for i in range(1,N+1):
		for j in range(1,N+1):
			
			new_diff = math.fabs(float(i)/float(j) - target)
			
			# Calculate A/B and compare it to target
			if new_diff < diff:
				# Change the old vals to the new closest pair
				diff = new_diff
				closest_A = i
				closest_B = j
				
				# print improvements on A and B
				print(" %3i / %3i, diff = %.8f" % (closest_A, closest_B, diff)) 
	
	# return results
	return closest_A, closest_B

# iteration 2
import fractions as frac

def closest_to_2(target):
	
	return frac.Fraction(target).limit_denominator(1000)
 


print(math.pi/4.0)

print(closest_to_2(math.pi/4.0))

closest_to(math.pi/4.0,1000)






