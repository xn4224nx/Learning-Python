import pylab as pyl

def moving_average (input_list, window_size):
	
	# cycle through the list
	for i in range(len(input_list)):
		
		# average the value over the window
		
		# take the slice we are using
		# input_list[i-window_size/2: i+window_size/2]
		
		# Take the moving average
		input_list [i] = sum(input_list[int(i-window_size/2): int(i+window_size/2)]) / window_size
	
	return input_list


# open the file
input_file = open('files/noisy_signal.txt')

line_num = 0
time_plot = []
noisy_plot = []
smooth_plot = []


for line in input_file:
	
	line_num += 1
	
	# Split the values from each line into arrays
	line_values = line.split()
	
	# Put the valuse in the file into arrays
	time_plot.append(float(line_values[0]))
	noisy_plot.append(float(line_values[1]))
	

# Copy list then smooth
smooth_plot = noisy_plot.copy()
smooth_plot = moving_average(smooth_plot,200)


# Plot data
pyl.subplot(211)
pyl.plot(time_plot,noisy_plot)
pyl.subplot(212)
pyl.plot(time_plot,smooth_plot)
pyl.show()

