import numpy as np
import math



def accending_order_1(N):
	
	# Repeat 1,000,000 times
	num_repeats = 1000000
	
	# Count of those instances in accending order
	count = num_repeats
	
	for i in range(num_repeats):
		
		# Generate 4 numbers between 0 -> 1
		x = np.random.uniform(0,1,N)
		
		#print(x)
		#print(count)
		
		# Test to see if they are in accending order
		for j in range(N-1):
			
			if x[j] > x[j+1]:
				count -= 1
				break
			
			
		
	# Calculate the probability of accending order and return
	print(count / num_repeats)
	return count / num_repeats

#accending_order_1(4)

def accending_order_2():
	
	# Repeat 1,000,000 times
	num_repeats = 1000000
	
	# Count of those instances in accending order
	count = num_repeats
	
	for i in range(num_repeats):
		
		
		# Generate 4 numbers between 0 -> 1
		x = np.random.uniform(0,1,4)
		
		
		if x[0] > x[1]:
			count -= 1
			continue
		if x[1] > x[2]:
			count -= 1
			continue
		if x[2] > x[3]:
			count -= 1
			continue

	# Calculate the probability of accending order and return
	print(count / num_repeats)
	return count / num_repeats

#accending_order_2()

from collections import deque

def accending_order_3(N):
	
	# Repeat 1,000,000 times
	num_repeats = 1000000
	
	# Count of those instances in accending order
	count = num_repeats
	
	# declare deque to be working with
	x = deque([])
	
	for i in range(N):
		x.append(np.random.uniform(0,1))
		
	# generate number on the fly and test if the last four numbers were in accending order
	
	for i in range(num_repeats):
		# put a new number in the array
		x.append(np.random.uniform(0,1))

		# remove a number from the array
		x.popleft()
		
		# Test to see if they are in accending order
		for j in range(N-1):
			
			if x[j] > x[j+1]:
				count -= 1
				break
		
	# return the probability of accending
	
	print(count / num_repeats)
	return count / num_repeats

accending_order_3(4)
