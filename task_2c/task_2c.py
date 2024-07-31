'''
*****************************************************************************************
*
*        		===============================================
*           		GeoGuide(GG) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 2C of GeoGuide(GG) Theme (eYRC 2023-24).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''
############################## FILL THE MANDATORY INFORMATION BELOW ###############################

# Team ID:			gg_2651
# Author List:		Vikas Tiwari , Vandana S , Reeba Gurupriya 
# Filename:			task_2c.py
# Functions:	    [`classify_event(image)` ,' arena_image(arena_path)',' event_identification(arena)']
###################################################################################################

# IMPORTS (DO NOT CHANGE/REMOVE THESE IMPORTS)
from sys import platform
import numpy as np
import subprocess
import cv2 as cv       # OpenCV Library
import shutil
import ast
import sys
import os

# Additional Imports
'''
You can import your required libraries here
'''
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# DECLARING VARIABLES (DO NOT CHANGE/REMOVE THESE VARIABLES)
arena_path = "arena.png"            # Path of generated arena image
event_list = []
detected_list = []

# Declaring Variables
'''
You can delare the necessary variables here
'''

# EVENT NAMES
mean = [0.5, 0.5, 0.5]
std = [0.25, 0.25, 0.25]
data_transform = transforms.Compose([
    transforms.Resize((65, 65)),
    transforms.ToTensor(),
    transforms.Normalize(mean, std)
])
class_names = ['combat','destroyedbuilding','fire','humanitarianaid','militaryvehicles']
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 5)  # Adjust the output layer to match your class count
model.load_state_dict(torch.load('trained_model.pth'))
model.eval()  # Set the model to evaluation mode
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)
'''
We have already specified the event names that you should train your model with.
DO NOT CHANGE THE BELOW EVENT NAMES IN ANY CASE
If you have accidently created a different name for the event, you can create another 
function to use the below shared event names wherever your event names are used.
(Remember, the 'classify_event()' should always return the predefined event names)  
'''
combat = "combat"
rehab = "humanitarianaid"
military_vehicles = "militaryvehicles"
fire = "fire"
destroyed_building = "destroyedbuilding"

# Extracting Events from Arena
def arena_image(arena_path):            # NOTE: This function has already been done for you, don't make any changes in it.
    ''' 
	Purpose:
	---
	This function will take the path of the generated image as input and 
    read the image specified by the path.
	
	Input Arguments:
	---
	`arena_path`: Generated image path i.e. arena_path (declared above) 	
	
	Returns:
	---
	`arena` : [ Numpy Array ]

	Example call:
	---
	arena = arena_image(arena_path)
	'''
    '''
    ADD YOUR CODE HERE
    '''
    frame = cv.imread(arena_path)
    arena = cv.resize(frame, (700, 700))
    return arena 

def event_identification(arena):        # NOTE: You can tweak this function in case you need to give more inputs 
    ''' 
	Purpose:
	---
	This function will select the events on arena image and extract them as
    separate images.
	
	Input Arguments:
	---
	`arena`: Image of arena detected by arena_image() 	
	
	Returns:
	---
	`event_list`,  : [ List ]
                            event_list will store the extracted event images

	Example call:
	---
	event_list = event_identification(arena)
	'''
    gray_arena = cv.cvtColor(arena, cv.COLOR_BGR2GRAY)

    # Apply thresholding to separate white boxes
    _, thresholded = cv.threshold(gray_arena, 200, 255, cv.THRESH_BINARY)

    # Find contours of white boxes
    contours, _ = cv.findContours(thresholded, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Iterate through the contours and extract bounding boxes
    for i, contour in enumerate(contours):
        x, y, w, h = cv.boundingRect(contour)
        # Calculate and print the length of the box
        box_length = np.sqrt((w)*(h))
        if (box_length > 65 and box_length < 73):

            # Extract the image region corresponding to the detected white box
            extracted_image = arena[y:y+h, x:x+w]
            #####################################################################################
            # extracted_image = cv.resize(extracted_image, (224, 224), interpolation=cv.INTER_LINEAR)
            extracted_image = extracted_image[15:-15, 15:-15]
            #####################################################################################

            # Save the extracted image region to the specified directory
            extracted_image_filename = f'extracted_{i}.jpg'
            cv.imwrite(f'extracted_{i}.jpg', extracted_image)
            event_list.append(extracted_image_filename)
    # print(event_list)
    return event_list

# Event Detection
def classify_event(image,model=model):
    image = Image.open(image)
    input_tensor = data_transform(image).unsqueeze(0).to(device)  # Preprocess the image and add a batch dimension

    with torch.no_grad():
        output = model(input_tensor)
        _, predicted_class = torch.max(output, 1)

    predicted_class_index = predicted_class.item()
    event = class_names[predicted_class_index]
    return event

# ADDITIONAL FUNCTIONS
'''
Although not required but if there are any additonal functions that you're using, you shall add them here. 
'''
###################################################################################################
########################### DO NOT MAKE ANY CHANGES IN THE SCRIPT BELOW ###########################
def classification(event_list):
    for img_index in range(0,5):
        img = event_list[img_index]
        detected_event = classify_event(img)
        print((img_index + 1), detected_event)
        if detected_event == combat:
            detected_list.append("combat")
        if detected_event == rehab:
            detected_list.append("rehab")
        if detected_event == military_vehicles:
            detected_list.append("militaryvehicles")
        if detected_event == fire:
            detected_list.append("fire")
        if detected_event == destroyed_building:
            detected_list.append("destroyedbuilding")
    os.remove('arena.png')
    return detected_list

def detected_list_processing(detected_list):
    try:
        detected_events = open("detected_events.txt", "w")
        detected_events.writelines(str(detected_list))
    except Exception as e:
        print("Error: ", e)

def input_function():
    if platform == "win32":
        try:
            subprocess.run("input.exe")
        except Exception as e:
            print("Error: ", e)
    if platform == "linux":
        try:
            subprocess.run("./input")
        except Exception as e:
            print("Error: ", e)

def output_function():
    if platform == "win32":
        try:
            subprocess.run("output.exe")
        except Exception as e:
            print("Error: ", e)
    if platform == "linux":
        try:
            subprocess.run("./output")
        except Exception as e:
            print("Error: ", e)

###################################################################################################
def main():
    ##### Input #####
    input_function()
    #################

    ##### Process #####
    arena = arena_image(arena_path)
    event_list = event_identification(arena)
    detected_list = classification(event_list)
    detected_list_processing(detected_list)
    ###################

    ##### Output #####
    output_function()
    ##################

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        if os.path.exists('arena.png'):
            os.remove('arena.png')
        if os.path.exists('detected_events.txt'):
            os.remove('detected_events.txt')
        sys.exit()
