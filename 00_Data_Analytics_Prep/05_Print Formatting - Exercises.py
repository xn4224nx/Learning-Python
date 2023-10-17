#### Pulse Data Exercise ####

import pylab as pyl 

#### Load the pulse data from the file into an array

pulse_data = []
infile = open("files/pulse_data.txt","r")
line_num = 0

for line in infile:
	line_num += 1
	pulse_data.append(float(line))
	# print (pulse_data[line_num-1])

# print(len(pulse_data))
infile.close()	

#### Create x values for the plot

x_vals = []
for i in range(len(pulse_data)):
	x_vals.append(float(i))

#### Sort the array then plot

sorted_pulse_data = pulse_data.copy()
sorted_pulse_data.sort()

pyl.subplot(211)
pyl.plot(x_vals, pulse_data)
pyl.subplot(212)
pyl.plot(x_vals, sorted_pulse_data)

pyl.show()

#### Data Binning ####

#### Setting up the data bins

num_bins = 50		# the number of bins the data is being sorted into
bin_result = []		# storing the number of results for each bin

for i in range(num_bins):
	bin_result.append(0)	# fill the bins with zero

#### Determine the range of data

min_val = min(pulse_data)
max_val = max(pulse_data)

data_range = max_val - min_val

#### Cycle through the data and determine the assignment of each value

for i in range(len(pulse_data)):
	
	# Working the bin for each value
	bin_id = int(num_bins * (pulse_data[i] - min_val ) / data_range)
	
	# Catch a problem with the final bin
	if bin_id == num_bins:
		bin_id = num_bins -1
	
	# Updating bin_result with the bin id
	bin_result[bin_id] += 1
	
#### Plot the values in a bar chart

x_vals_bin = []

for i in range(len(bin_result)):
	x_vals_bin.append(min_val + (i * max_val) / int(len(bin_result)) )

pyl.bar(x_vals_bin, bin_result)
pyl.show()

# or the easy way
pyl.hist(pulse_data,50)
pyl.show()
