import pylab as pyl

def plot_fx (start_x, end_x):
	
	# empty arrays for the data
	x_plot = []
	f_plot = []
	g_plot = []
	
	# Generating values for f(x) = x^2 + 20
	# Generating values for g(x) = (x/2)^3 - 100
	
	for i in range(start_x, end_x+1):
	
		# Generating x values
		x_plot.append(i)
		
		# Generating f(x) values
		f_plot.append(i*i + 20)
		
		# Generating g(x) values
		g_plot.append((i*0.5)**3 - 100)
		
	#print (x_plot)
	#print (f_plot)
	
	# plotting data
	pyl.plot(x_plot,f_plot)
	pyl.plot(x_plot,g_plot)
	pyl.legend(['y = x^2 + 20', 'y = (x/2)^3 - 100'], loc='upper left')
	
	pyl.show()
	
# test call of the function
plot_fx (12,14)
