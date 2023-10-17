####	Algorithms, control and conditionals	####
####	Part 2 - ATM Control Program			####

# Definition of the cashpoint function

def cashpoint (truepin, balance):
	
	# Ask the user to input the pin
	if( pin_check(truepin) != True):
		return(0, balance)
	
	# Give the user options on what they want
	print ("\nPlease choose your transaction type")
	print ("   - to request a balance  - enter 1")
	print ("   - to make a withdrawal  - enter 2")
	print ("   - to top-up a telephone - enter 3")
	
	user_choice = float(input("Enter your choice: "))
	
	# input 1 for solely checking balance
	if (user_choice == 1):
		print ("\nYour current balance is: £", balance)
		return(user_choice, balance)
	
	# input 2 for withdrawal
	if (user_choice == 2):
		balance = withdrawal(balance)
		return(user_choice, balance)
	
	# input 3 for phone top up
	if (user_choice == 3):
		balance = mobileTopUp(balance)
		return(user_choice, balance)
	
	else:
		print("Sorry command not recognised.")
		return(user_choice, balance)

def pin_check (truepin):
	# Ask the user to input the pin
	user_pin = input("Please enter your pin: ")
	
	# Check to see if the pin is correct
	if (user_pin != truepin):
		print ("Pin incorrect")
		return False
	else:
		print ("Pin correct")
		return True

def withdrawal (balance):
	
	maxamount = 100.00
	
	print ("Withdrawal amount must be a multiple of 10 pounds.")
	amount = float(input("Please enter your withdrawal amount: £"))
	
	# Chack if a multiple of ten
	if (multipleOfTen(amount) != True):
		print ("Sorry the amount needs to be a multiple of ten.")
		return(balance)
	
	
	# Check on validity of user input
	if (amount > maxamount):
		print ("Sorry the maximum amount allowed is £", maxamount)
		return (balance)
		
	elif (amount > balance):
		print ("Sorry you only have £", balance, " in your account.")
		return (balance)
	
	# Giving the cash and modifying the balance
	else:
		print("Dispensing £",amount)
		balance = balance - amount
		
		# Returns new balance
		return (balance)

def mobileTopUp(balance):
	maxTopUp = 100.00
	print ("Please enter the number of the mobile phone you wish to top-up: ",)
	number1 = int(input())
	print ("Please RE-enter the number of the phone: ",)
	number2 = int(input())
    
	if (number1 != number2):
		print ("Numbers do not match")
		return (balance)
	else:
		amount = int(input("please enter the ammount you wish to top-up: £"))
		if (amount > maxTopUp):
			print ("Sorry £", amount," is too much, the max amount is £", maxTopUp)
			return (balance)
		elif (amount > balance):
			print ("Sorry you only have £", balance, " in your account.")
			return (balance)
		
		return (balance - amount)

def multipleOfTen(amount):
    return ( float(amount) > 0 and float(amount) % 10 == 0)  
	
# Test calls to the program

print ('TEST-EXAMPLE 1')
result = cashpoint('1234', 15.55)
print ('---------\nRESULT:', result)
print ('-' * 50, '\n')
