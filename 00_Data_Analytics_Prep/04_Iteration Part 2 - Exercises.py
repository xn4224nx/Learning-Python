def sum_list (input_list):
	
	total = 0
	
	for i in range(len(input_list)):
		 total += input_list[i]
		 
	return total
	
# Test call of the function
print (sum_list([3,4,5]))

def triangular_num (start_num):
	
	total = 0
	
	while start_num > 0:
		
		total += start_num
		
		start_num -= 1
	
	return total

def square_list (input_list):
	
	# make a copy of the input list
	copy_list = list(input_list)
	
	# cycle through the list and square every number in it
	
	for i in range(len(copy_list)):
		
		copy_list[i] = copy_list[i] * copy_list[i]
	
	return copy_list


# Test call of the function
x = [3,4,5]

print(square_list(x))
print(x)

def triang_list (input_list):
	
	# Convert every num in a list to a triangular number
	
	for i in range(len(input_list)):
		
		input_list[i] = triangular_num(input_list[i])
	
	return input_list

# test call of the function
print(triang_list([1,2,3,4,5,6,7,8,9,10]))
	
