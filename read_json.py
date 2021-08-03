#!/usr/bin/python

import json
import cv2 as cv
import numpy as np

SCALE = 5
BACKGROUND = 30 * SCALE
OFFSET = 50

# Window name in which image is displayed
window_name = 'Image'


# Opening JSON file 
with open('data_rev4.json') as json_file:
	data = json.load(json_file)
	
	#package size
	package = data['package']
	length = int(float(package[0]['length']) * SCALE) 
	width = int(float(package[0]['width']) * SCALE)
	
	# Create a base image
	img = np.zeros((length+BACKGROUND,width+BACKGROUND,3), np.uint8)
	print(length+BACKGROUND,width+BACKGROUND)
	#Create package edge
	cv.rectangle(img,(OFFSET,OFFSET),(width +OFFSET,length +OFFSET),(255,255,255),1)
	
	#pins
	for pin in data['pins']: 
		location_x = int(float(pin["location_x"]) * SCALE)
		location_y = int(float(pin["location_y"]) * SCALE)
		cv.circle(img,(location_x+OFFSET, location_y+OFFSET), 1, (0,0,255), -1)
		
	#pins
	for target in data['target']: 
		location_x = int(float(target["location_x"]) * SCALE)
		location_y = int(float(target["location_y"]) * SCALE)
		cv.circle(img,(location_x+OFFSET, location_y+OFFSET), 2, (0,0,255), -1)

# Displaying the image 
cv.imshow(window_name, img) 

cv.waitKey(0)