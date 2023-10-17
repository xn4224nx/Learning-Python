#### Part 5 -  Printing to a file ####

# Opening the file
out = open('junk_output/outputfile.txt','w')

# Writing text to the output file
print ('some output string', file = out)

#### Printing formatted numbers

# %d means integer, the 5 represents the spaces
x = [7, 344, 12]
for i in x:
    print ('%5d' % (i))

# %f is a float the .3 denotes decimal places
# the 10 denotes the min width (includes decimal places)

x = [7.66666, 343.2, 11.12]
for i in x:
    print ('|%10.3f|' % (i))
    
# %s is the string type

####	More File Handling 

#### Self contained file opening and closing

import sys	# required

with open('files/george04.txt','r') as import_file:
	
	num = 0
	
	for line in import_file:
		num += 1
		print ('[%02d] %s' % (num, line), end = "")


#### Explicit file closing

infile = open("files/george04.txt", "r")
outfile = open("junk_output/copyofgeorge04.txt", "w")

num = 0

# Read the file in and the output to file line by line
for line in infile:
	num += 1
	print ("[%02d] %s" % (num,line), end = "",file = outfile)

# Closing the files
infile.close()
outfile.close() 


