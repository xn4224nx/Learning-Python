#### Dictionaries and Sorting ####

#### Initalising a Dictionary

phonebook = {}

phonebook["Dave"] = "01246551313"
phonebook["Lisa"] = "01246551314"
phonebook["Sam"] = "01246551315"
phonebook["Maisy"] = "01246551316"

print(phonebook)

#### Accessing Values and Updating

print(phonebook["Sam"])				# Access a value
phonebook["Lisa"] = "07422342234"	# update a value
phonebook["Ben"] = "01246551317"	# Add a value to the dict
del phonebook["Maisy"]				# delete a value
print(phonebook.keys())				# Print the dict keys
print(list(phonebook.keys()))		# Print the keys as a list
print(list(phonebook.values()))		# Print the values in the dict
print("Maisy" in phonebook)			# Check if key is in the dict

#### Accessing an uncertain value

k = "Sam"

if k in phonebook:
	print(k, ":", phonebook[k])	# This line could crash the code if k is MIA
else:
	print(k, "not found!")

#### Printing Dict from a loop

for n in phonebook:
	print(n, ":", phonebook[n])

#### Sorting Objects in Python

x = [4,7,10,1,45,5,0,-10]

print(sorted(x))				# Show the object sorted but doesn't modify
print(sorted(x,reverse=True))	# Reverse Sort
print(x)
x.sort()						# Permenantly sorts
print(x)

# Sorting via key or value

x = [('a', 3), ('c', 1), ('b', 5)]
print(sorted(x, key=lambda s:s[0]))	# Sort by the 1st thing in the turple, the letters
print(sorted(x, key=lambda s:s[1]))	# Sort by the 2nd thing in the turple, the No.s

# Print by sorted key
for n in sorted(phonebook):
	print(n, ":", phonebook[n])

# Print by the sorted value
for n in sorted(phonebook, key=lambda s:s[1]):
	print(n, ":", phonebook[n])
	
# Print with numeric values
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals = densities.keys()
# Sort a list of the key based on the value sizes
metals_list = sorted(metals,reverse=False,key=lambda m:densities[m])

for metal in metals_list:
    print ('%8s = %5.1f' % (metal,densities[metal]))

# Sort a dictionary by turing it into a turple

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
sorted_densities = sorted(densities.items(), key=lambda kv: kv[1])
print(sorted_densities)


















