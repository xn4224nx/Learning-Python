#### Dictionaries and Sorting - Moby Dick Excercise ####

# Task is to count the number of different words in the novel moby dick

#### fn readstopwords: takes in the address of txt file, returns an array of words
def readstopwords(file_address):
		
	# Open the file of stop words and read into an array
	infile_stopwords = open(file_address, "r")
	
	return_array = []
	
	for line in infile_stopwords:
		return_array.append(line.strip())
	
	
	# Close stopfile
	infile_stopwords.close()
	
	return return_array


#### fn countwords: takes in the address of the txt file and return the dict of word counts
def countwords(file_address,stop_word_array):
	
	# Open the file to count 
	infile = open(file_address, "r")
	
	# dict("the word", the frequency of the word)
	file_words = {}

	# Read the file in
	for line in infile:
	
		line_contents = []			# wipe at each line to ensure no overlap
	
		# Read the current line and use split to put it into an array
		line_contents = line.split()
		# print(line_contents)
		
		for n in range(len(line_contents)):
			# check if the word is a stop word, so don't count it
			if line_contents[n] in stop_word_array:
				continue
			
			# Check each member in that array against the dict if they are not in add them
			if line_contents[n] not in file_words:
				file_words[line_contents[n]] = 1
			
			# otherwise update the count of their dict entry
			elif line_contents[n] in file_words:
				file_words[line_contents[n]] += 1
	
	# Closing the files
	infile.close()
	
	# return the dict of word counts
	return file_words


#### fn printtop20: print the 20 sets with the highest VALS
def printtop20 (dictionary):
	words = dictionary.keys()

	# Sort a list of the key based on the value sizes
	word_list = sorted(words,reverse=True,key=lambda m:dictionary[m])
	count = 0
	for words in word_list:
		if count >= 20:
			break
		print ('%14s = %02i' % (words,dictionary[words]))
		count += 1

# test call of the functions
badwords = readstopwords("files/stopwords.txt")
mobywords = countwords("files/mobydick.txt", badwords )
printtop20(mobywords)
