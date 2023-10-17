##### Print Function
 
print (2+4.6)
print ("Test")
print ()			# Prints a newline, the "\n" functions as well
print ("The answer is ", 34.5 , ", to 3 sig fig.\n")

##### Variables

x = 0.345
y = 3
print (x)
print (x + 3*y)
x = x + 1 
print (x)

##### Strings

s1 = "Hello " 	# Defining a string
s2 = "World! "

print (s1 + s2)
print (s1 * 10)
print (s1 + s2 * 10)

##### More Printing

print ("hello", end="")  # end="" sets the end char
print (" again")		 # its usually \n
print ("hello\n\nthere")

##### Taking input from the user


miles = input("Input the no. of miles: ")	# miles is currently a string

# Use float() to change it into a number

kilometers = (float(miles) * 8.0) / 5.0			
print("Converting distance in miles to kilometers:")
print("Distance in miles: ", miles)
print("Distance in kilometers: ", kilometers)

##### Converting Temperatures

# Ask the user for temperature in degrees Celsius
cels = float(input("\n\n\nInput the temperature in degrees Celsius: "))

# Calculate the temp in faranheit
fara = ((cels * 9) / 5 ) + 32

# Calculate the temp in kelvin 
kelvin = cels + 273.15

# Display the three temps
print ("Tempature in Celsius: ", cels, "°C" )
print ("Tempature in Faranheit: ", fara, "°F" )
print ("Tempature in Kelvin: ", kelvin, "k" )

##### Functions in Python

# indentaion is important!!

# Defining the function
def convert_temp(cels):
	fara = ((float(cels) * 9) / 5 ) + 32
	kelvin = float(cels) + 273.15
	
	print ("Tempature in Celsius: ", cels, "°C" )
	print ("Tempature in Faranheit: ", fara, "°F" )
	print ("Tempature in Kelvin: ", kelvin, "k" )

# Calling the function

convert_temp(44)

convert_temp(125.5)

##### Functions returning values
def convert_temp2(cels):
	fara = ((float(cels) * 9) / 5 ) + 32
	return fara

print (convert_temp2(50))


