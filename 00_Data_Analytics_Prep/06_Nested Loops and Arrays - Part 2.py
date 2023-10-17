#### Images as Arrays ####

#### Display an image

# The image has been imported as intensity values in an array

import pylab as pyl
img = pyl.imread('pictures/chick.png')
print (img.shape, "\n")

pyl.imshow(img)
pyl.show()

# Modifying intensities in the array
(d1,d2,d3) = img.shape

for i in range(d1):
    for j in range(d2):
        for k in range(d3):
            img[i,j,k] = 1 - img[i,j,k]	# Invert the RBG values
            
pyl.imshow(img)
pyl.show()

# Modifying the RBG values in the array

(d1,d2,d3) = img.shape
for i in range(d1):
    for j in range(d2):
        pixel = img[i,j]
        if sum(pixel) < 1.5:
            img[i,j] = (.99, .0, .0) # Set the values to red
            
pyl.imshow(img)
pyl.show()
