#### Che Guevara Excercise ####

#### Import Che Guevara Image then display

import pylab as pyl

orig_img = pyl.imread('pictures/che.png')


pyl.imshow(orig_img)
pyl.show()

#### Task 1 - Strong Monochrome

mono_img = orig_img.copy()
(d1,d2,d3) = mono_img.shape

# Go through the image and trun everything to white or black

for i in range(d1):
	for j in range(d2):
		pixel = mono_img[i,j]
		if sum(pixel) < 1.5:
			# if light gray turn to white
			mono_img[i,j] = (.0, .0, .0)
		else:
			# if dark gray turn to black
			mono_img[i,j] = (1, 1, 1)

# Display monochrome image
pyl.imshow(mono_img)
pyl.show()

#### Task 2 - Red and black

red_img = orig_img.copy()
(d1,d2,d3) = red_img.shape

# Go through the image and turn everything to red or black

for i in range(d1):
	for j in range(d2):
		pixel = red_img[i,j]
		if sum(pixel)/3 > 0.5 :
			# if light gray turn to red
			red_img[i,j] = (1.0, .0, .0)
		else:
			# if dark gray turn to black
			red_img[i,j] = (0, 0, 0)


# Display monochrome image
pyl.imshow(red_img)
pyl.show()


#### Task 3 - White Face, red background, black otherwise

face_img = orig_img.copy()
(d1,d2,d3) = face_img.shape

print

for i in range(d1):
	for j in range(d2):
		
		# Check to see if in face region
		if 50 < i < 158 and 50 < j < 133:
			
			pixel = face_img[i,j]
			if sum(pixel) < 1.5:
				# if light gray turn to white
				face_img[i,j] = (.0, .0, .0)
			else:
				# if dark gray turn to black
				face_img[i,j] = (1, 1, 1)
			
			continue
		
		# if not face normal rules
		pixel = face_img[i,j]
		if sum(pixel)/3 > 0.5 :
			# if light gray turn to red
			face_img[i,j] = (1.0, .0, .0)
		else:
			# if dark gray turn to black
			face_img[i,j] = (0, 0, 0)

# Display face image
pyl.imshow(face_img)
pyl.show()

#### Task 4 - Funky Colours

funk_img = orig_img.copy()
(d1,d2,d3) = funk_img.shape

for i in range(d1):
	for j in range(d2):


			if sum(funk_img[i,j]) > 2:
				# Turn the colour to red
				funk_img[i,j] = (1.0, .0, .0)

			elif sum(funk_img[i,j]) < 1:
				# Turn the colour to blue
				funk_img[i,j] = (.0, 1.0, .0)

			else:
				# Turn the colour to green
				funk_img[i,j] = (.0, .0, 1.0)


pyl.imshow(funk_img)
pyl.show()


#### Task 5 - Chick on Che

# make a copy of the che img
combined_img = orig_img.copy()
(d1,d2,d3) = combined_img.shape

# import the chick image
chick_img = pyl.imread('pictures/chick.png')

# Cycle through the Che image and replace the face
for i in range(d1):
	for j in range(d2):
		
		# Check to see if in face region
		if 50 < i < 100 and 50 < j < 100:
			
			combined_img[i,j] = chick_img[i-47,j-32]


pyl.imshow(combined_img)
pyl.show()


































