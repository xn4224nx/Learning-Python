####	Algorithms, control and conditionals	####

####	Booleans Definitions
#		
#		==  : equal to
#		>   : greater than
#		>=  : greater than or equal to
#		<   : less than
#		<=  : less than or equal to
#		!=  : not equal to

print (3 == 3)
print ("this" == "this")
print (3 >= 4)
print ("This" == "this")
print ("string" != 4)


print (4 < 5 and 6 < 7 )
print (3 >= 4 or 3 != 1 )

####	Conditionals

age = 56

if age >= 70:
	print ("You may collect your pension.")
else:
	print ("Back to work pleb.")
# the else statement is optional

age = 17

if age < 2:
	print  ("off to your parents")
elif age < 5:
	print  ("off to nursary")
elif age < 11:
	print  ("off to primary school")
elif age < 18:
	print  ("off to secondry school")
elif age < 21:
	print  ("off to university")
else: 
	print  ("off to work")

####	Return Functions

def is_odd(n):
	if (n % 2 == 0):
		return False
	else:
		return True
	
print (is_odd(-67))
