#### Classifying the tiger weights

import numpy as np
import matplotlib.pyplot as plt

#### Previous functions
def rnd_sample(data, N):
	chosen = np.random.choice(data.shape[1], N, replace=False)
	sample = data[0, chosen]		# 0 ensures the first row is taken

	return sample


# Import the tiger data
female_tigers = np.loadtxt(open("files/female_tigers.txt","rb"))
male_tigers = np.loadtxt(open("files/male_tigers.txt","rb"))
print("Data Imported")

# Plot histograms of the tiger weights

plt.subplot(2,2,1)
plt.hist(female_tigers[0,:], 100)
plt.hist(male_tigers[0,:], 100)

plt.subplot(2,2,2)
plt.hist(male_tigers[0,:], 100)
plt.hist(female_tigers[0,:], 100)

plt.subplot(2,2,3)
plt.hist(female_tigers[0,:], 100)

plt.subplot(2,2,4)
plt.hist(male_tigers[0,:], 100)

plt.show() # This showed that 275 would be a good cut off


# take a random sample of 100 tigers 
chosen_female = rnd_sample(female_tigers,100)
chosen_male = rnd_sample(male_tigers,100)


# Plot histograms of the tiger weights
plt.subplot(2,2,1)
plt.hist(chosen_female, 100)
plt.hist(chosen_male, 100)

plt.subplot(2,2,2)
plt.hist(chosen_male, 100)
plt.hist(chosen_female, 100)

plt.subplot(2,2,3)
plt.hist(chosen_female, 100)

plt.subplot(2,2,4)
plt.hist(chosen_male, 100)

plt.show()
