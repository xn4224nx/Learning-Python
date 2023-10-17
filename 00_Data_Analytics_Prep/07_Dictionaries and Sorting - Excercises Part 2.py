#### Dictionaries and Sorting - Text Comparison Excercise ####



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



#### Function takes file address and the returns a dict with the unique words in a dict
def unique_words(file_address, stop_words_file):
	
	# return dict
	return_dict = {}
	
	# open stop words file
	stop_words = readstopwords(stop_words_file)
	
	# open file to get unique words
	infile = open(file_address, "r")
	
	for line in infile:
		
		line_contents = []
		line_contents = line.split()
		
		for n in range(len(line_contents)):
			
			# check if the word is a stop word
			if line_contents[n] in stop_words:
				continue
			
			# check if the word is in the dict
			if line_contents[n] in return_dict:
				continue
			
			# Check each member in that array against the dict if they are not in add them
			else:
				return_dict[line_contents[n]] = 1
			
		
	# Closing the files
	infile.close()
	
	# returning the dict
	return return_dict


#### function takes in two file addresses in and calculates lexical overlap

# The lexical overlap is the number of words both texts share, word count is not important

def lexical_overlap(first_file, second_file, stop_words_file):
	
	overlap_count = 0
	
	# Read the first text file and put each unique word in a dictionary
	first_dict = unique_words(first_file, stop_words_file)
	
	# Read the second text file and put each unique word in a dictionary
	second_dict = unique_words(second_file, stop_words_file)
	
	# Iterate over the first dict and see if each word is in the second dict
	for i in first_dict:
		for j in second_dict:
			if i == j:
				#print( i, ":", j)
				# update the count when ever a word is in both
				overlap_count += 1
	
	# print("The number of overlapping words is: ",overlap_count)	
	
	# Calculate the similarity score and return
	return overlap_count/ (len(first_dict) + len(second_dict) - overlap_count)
		
	

# test of the functions

#print(unique_words("files/george02.txt"))
print('%10.3f' % lexical_overlap("files/george01.txt","files/george02.txt","files/stopwords.txt"))
print('%10.3f' % lexical_overlap("files/george01.txt","files/george03.txt","files/stopwords.txt"))
print('%10.3f' % lexical_overlap("files/george01.txt","files/george04.txt","files/stopwords.txt"))
print('%10.3f' % lexical_overlap("files/george02.txt","files/george03.txt","files/stopwords.txt"))
print('%10.3f' % lexical_overlap("files/george02.txt","files/george04.txt","files/stopwords.txt"))
print('%10.3f' % lexical_overlap("files/george03.txt","files/george04.txt","files/stopwords.txt"))
