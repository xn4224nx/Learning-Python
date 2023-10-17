# Lists

x = ['this', 55, 'that']
print (x[0])
print (x[1])
print (x[2])

# Adding to Lists

x = ['aa', 'bb', 'cc']
x[1] = 33
print (x)

x.append('dd') # This command adds the item to the end of the list
print (x)

# Concaternating Lists

x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y
print (z)

# Extracting part of a list

print (z[3:10]) # This ( ,) is a turple, they are immutable 
print (z[8:10]) # But they behave as list in python

# For Loops

values = [875, 23, 451]

for val in values:
    print ('-->', val)

# For can iterate over a turple
for char in "Yes":
    print (char)

# Summing over a list
values = [3, 12, 9]
total = 0
for val in values:
    total += val
print ('TOTAL:', total)

# Range function
# list() converts  to list type

print (list(range(3)))   # First value is the 'range'
print (list(range(4,9))) # Second value is end of the range
print (list(range(0,101,10))) # Third value is the step

# Incrementing values in a list by one
vals = [8, 12, 10, 34]
print (len(vals))		# len() returns the numerical lenght of a list

# Add one to every item in the list
for i in range(len(vals)):
	vals[i] += 1
print (vals)

# Times every item in the list by 2
for i in range(len(vals)):
    vals[i] = vals[i] * 2
print (vals)
