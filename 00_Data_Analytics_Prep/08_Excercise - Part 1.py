# Exercise 1

# fn sum_of_reciprocals: takes a +ve integer input and returns a sum of values
def sum_of_reciprocals(end_val):
	
	total_sum = 0
	n = 1
	
	while n < end_val+1:
		
		total_sum += 1/n
		n += 1
	
	return total_sum

# testing the fn
print(sum_of_reciprocals(1))
print(sum_of_reciprocals(2))
print(sum_of_reciprocals(3))
print(sum_of_reciprocals(4))
print(sum_of_reciprocals(5))



# Exercise 2

# fn add_numlists: takes two lists as inputs

def add_numlists(list_1, list_2):

	# if the lists are different lengths return None 
	if len(list_1) != len(list_2):
		return None
	
	return_list = []
	
	# otherwise return one list with each element from the two lists added together 
	for n in range(len(list_1)):
		return_list.append(list_1[n]+list_2[n])
	
	return return_list

# testing the fn
x = [1,2,3,4,5,8,-1,5,3]
y = [3,6,3,2,1,1,-9,2,5]

print(add_numlists(x,y))


# Exercise 3

# fn pos_numlist: takes an array, returns True if all +ve, otherwise false

def pos_numlist(input_list):
	
	# returns false on empty list
	if len(input_list) < 1:
		return False
	
	for n in range(len(input_list)):
		
		if input_list[n] < 0:
			return False
	
	return True

# testing the fn
z = []
print(pos_numlist(z))





