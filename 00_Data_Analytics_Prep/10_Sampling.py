#### Using sampling to estimate the mean and the variance ####

import numpy as np
import matplotlib.pyplot as plt

# Col 1:  weight, Col 2: length

# Importing the data from the files
female_tigers = np.loadtxt(open("files/female_tigers.txt","rb"))
male_tigers = np.loadtxt(open("files/male_tigers.txt","rb"))

# Computing the true mean and variance
print(np.mean(female_tigers, axis=1))
print(np.var(female_tigers, axis=1))

# Take a sample of the data
sample = female_tigers[:, 1:20]		# take the first 20
print(np.mean(sample, axis=1))
print(np.var(sample, axis=1))

# Take a random repeated sample

# female_tigers.shape[1] is the max to choose from ie 1250
# replace=False means if it has picked a entry it won't pick it again
repeated_sample = np.random.choice(female_tigers.shape[1], 20, replace=False)
sample = female_tigers[:, repeated_sample]

print(np.mean(sample[0,:]))		# set 0 to 1 to find the length
print(np.var(sample[0,:]))

#### Sampling Function

def sample_stats(data, N):
    chosen = np.random.choice(data.shape[1], N, replace=False)
    sample = data[:, chosen]
    mean_estimate = np.mean(sample, axis=1)
    var_estimate = np.var(sample, axis=1)
    return mean_estimate, var_estimate
    

def do_sampling(data, n_repeats):
	
	sample_sizes = [2, 5, 10, 20, 40, 100]
	
	sample_means = np.zeros((2,n_repeats))
	sample_vars = np.zeros((2,n_repeats))

	for j in range(len(sample_sizes)):

		for i in range(n_repeats): 
			sample_means[:,i],sample_vars[:,i]=sample_stats(female_tigers, sample_sizes[j])
	
		plt.subplot(2,3,j+1)	
		plt.hist(sample_means[0,:], 100)
		plt.hist(sample_means[1,:], 100)
		plt.hist(sample_vars[0,:], 100)
		plt.hist(sample_vars[1,:], 100)


	plt.show()
	return sample_means, sample_vars

do_sampling(female_tigers, 10000)

