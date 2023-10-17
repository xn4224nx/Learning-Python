from random import randint as randint_1

#### Iteration: while-loops and loop-control #### 

# while Loop
i =10

while  i <= 100:
	print (i)
	i = i + 1 


# Factorial Example

def Factorial(n):
	if (n == 0 or n == 1):
		return 1
	else:
		total = 1
		while n > 1:
			total = total * n
			n = n -1
	
	return total

print (Factorial(5))

# Guessing Game

def guess (attempts, range):
	
	# Generate the number to be guessed
	answer = randint_1 (1,range)
	
	# Test Print statement
	# print ("Answer = ", answer)
	
	print ("Welcome! Can you guess my secret number?")
	
	#Start the guessing loop
	while attempts > 0:
		
		print ("you have ", attempts, " guesses remaining")
		user_guess = float(input ("Make a guess: "))
		
		# User guesses correct leave the loop
		if (user_guess == answer):
			print ("Well done! You got it right")
			break
			
			
		elif (user_guess > answer):
			print ("No - too high!")
			
			
		elif (user_guess < answer):
			print ("No - too low!")
		
		attempts = attempts - 1
		
		if(attempts < 0):
			print ("No more guesses - bad luck! ")
	
	# Generic ending message
	print ("GAME OVER: thanks for playing. Bye.")
	
# Test call to function
# guess(3,20)

# Newton–Raphson method 	

def my_sqrt(A):
	
	# Initial guess for the method
	x = 1.0
	
	# Tolerance value epsilon
	error = 0.00001
	
	while abs(x*x - A) > error:
		
		# Calculate the new value of x
		x = x - (x*x-A)/(2*x)
	
	return x
	
print(my_sqrt(456))

def my_cubert(A):
	
	# Initial guess for the method
	x = 1.0
	
	# Tolerance value epsilon
	error = 0.000001   
	
	while abs(x*x*x - A) > error:
		
		# Calculate the new value of x
		x = x - (x*x*x-A)/(3*x*x)
	
	return x
	

print (my_cubert(56))
