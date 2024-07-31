'''
*****************************************************************************************
*
*        		===============================================
*           		Geo Guide (GG) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 4A of Geo Guide (GG) Theme (eYRC 2023-24).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			gg_2651
# Author List:		Vikas Kumar Tiwari , renukesh , Reeba Gurupriya
# Filename:			task_2c.py
# Functions:	    [`classify_event(image)` ,' arena_image(arena_path)',' event_identification(arena)']

####################### IMPORT MODULES #######################
from sys import platform
import numpy as np
import subprocess
import cv2 as cv       # OpenCV Library
import shutil
import ast
import time
import sys
import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import torchvision                         
##############################################################

arena_path = "image.png"            # Path of generated arena image
event_list = []
detected_list = []

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# EVENT NAMES
# Apply necessary transformations (same as during training)
transform = transforms.Compose([
    transforms.Resize(224),  # Resize to the expected input size
    transforms.ToTensor(),  # Convert to a PyTorch tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize the pixel values
])
class_names = ['combat','destroyedbuilding','fire','humanitarianaid','militaryvehicles']

# Load the model's state_dict from the saved file
model = torchvision.models.efficientnet_b0()  # Create an instance of the model
model.classifier = nn.Linear(1280, len(class_names))  
state_dict = torch.load("trained_model_nice.pth")
state_dict["classifier.weight"] = state_dict.pop("classifier.1.weight")
state_dict["classifier.bias"] = state_dict.pop("classifier.1.bias")
model.load_state_dict(state_dict)

combat = "combat"
rehab = "humanitarianaid"
military_vehicles = "militaryvehicles"
fire = "fire"
destroyed_building = "destroyedbuilding"

################# ADD UTILITY FUNCTIONS HERE #################
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
    arena = cv.imread(arena_path)
    return arena 

def event_identification(arena, boxes):        
    ''' 
    Purpose:
    ---
    This function will filter out events from the arena image based on the given bounding boxes.
    
    Input Arguments:
    ---
    `arena`: Image of arena detected by arena_image() 
    `boxes`: List of tuples (x, y, w, h) representing bounding boxes
    
    Returns:
    ---
    `event_list`: List of extracted event images

    Example call:
    ---
    event_list = event_identification(arena, boxes)
    '''

    event_list = []

    # Iterate through the bounding boxes
    for i, (x, y, w, h) in enumerate(boxes):
        # Ensure the coordinates and dimensions are within bounds
        x = max(0, x)
        y = max(0, y)
        w = min(w, arena.shape[1] - x)
        h = min(h, arena.shape[0] - y)

        # Extract the image region corresponding to the bounding box
        extracted_image = arena[y:y+h, x:x+w]
        if not extracted_image.size == 0:  # Check if the extracted image is not empty
            #####################################################################################
            # extracted_image = cv.resize(extracted_image, (224, 224), interpolation=cv.INTER_LINEAR)
            # extracted_image = extracted_image[10:-5, 10:-5]
            #####################################################################################

            # Save the extracted image region to the specified directory
            extracted_image_filename = f'extracted_{i}.jpg'
            cv.imwrite(extracted_image_filename, extracted_image)
            event_list.append(extracted_image_filename)

    return event_list

# Event Detection
def classify_event(image,model=model):
    image = Image.open(image)
    input_tensor = transform(image).unsqueeze(0).to(device)  # Preprocess the image and add a batch dimension
    model.eval() 
    with torch.no_grad():
        output = model(input_tensor)
    predicted_class_index = torch.argmax(output, dim=1)

    event = class_names[predicted_class_index.item()]
    return event

"""
You are allowed to add any number of functions to this code.
"""
def classification(event_list):
    for img_index in range(0,5):
        img = event_list[img_index]
        detected_event = classify_event(img)
        # print((img_index + 1), detected_event)
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
    # os.remove('arena.png')
    return detected_list

def detected_list_processing(detected_list):
    try:
        detected_events = open("detected_events.txt", "w")
        detected_events.writelines(str(detected_list))
    except Exception as e:
        print("Error: ", e)


def task_4a_return():

    # Open the default camera (usually the first camera connected)
    cap = cv.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Get the screen resolution
    screen_width = 1920  # Change this according to your screen resolution
    screen_height = 1080  # Change this according to your screen resolution

    # Calculate the width and height for the video window (left half of the screen)
    video_width = int(screen_width / 2)
    video_height = screen_height

    # Create a window to display the video feed
    cv.namedWindow("Camera Feed", cv.WINDOW_NORMAL)
    
    # Set the position and size of the window
    cv.resizeWindow("Camera Feed", video_width, video_height)
    cv.moveWindow("Camera Feed", 0, 0)  # Move window to the top-left corner
    
    leave = 0
    show_box = False

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Resize the frame to fit the video window size
        frame = cv.resize(frame, (video_width, video_height))

        # Display the frame
        cv.imshow("Camera Feed", frame)

        # Check for key press, if 'a' is pressed, capture a frame
        key = cv.waitKey(1)
        if key & 0xFF == ord('a'):
            # print("Capturing image in 1 second...")
            time.sleep(1)
            # Capture a frame after 1 second
            ret, frame = cap.read()
            # Save the captured frame as an image
            if ret:
                cv.imwrite("image.png", frame)
                # print("Image captured and saved as 'image.png'")
                show_box = True
                
                # major processing
                ######################################################################################
                arena = arena_image(arena_path) 
                event_list = event_identification(arena,boxes)
                detected_list = classification(event_list)
                detected_list_processing(detected_list)
                identified_labels = labeler()
                print(f'identified_labels = {identified_labels}')
                ######################################################################################
            else:
                print("Error: Unable to capture frame.")
                
        if ((leave == 1)or(key & 0xFF == ord('q'))):
                break 
        while show_box:
            # Draw boxes on the captured image
            # print("Drawing boxes...")
            key = cv.waitKey(1)
            if key & 0xFF == ord('q'):
                leave = 1
                break 
            ret, frame = cap.read()      
            for i, (x, y, w, h) in enumerate(boxes):
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv.putText(frame, detected_list[i], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            frame = cv.resize(frame, (video_width, video_height))
            # Display the frame with boxes
            cv.imshow("Camera Feed", frame)
            cv.waitKey(1)
                                   
    # Release the camera and close all OpenCV windows
    cap.release()
    cv.destroyAllWindows()

boxes = [
    (179, 421, 35, 32), (390, 330, 35, 36), (395, 239, 35, 37), (167, 240, 38, 37), (171, 82, 40, 40)
]
##############################################################

def labeler():
    """
    Purpose:
    ---
    Only for returning the final dictionary variable
    
    Arguments:
    ---
    You are not allowed to define any input arguments for this function. You can 
    return the dictionary from a user-defined function and just call the 
    function here

    Returns:
    ---
    `identified_labels` : { dictionary }
        dictionary containing the labels of the events detected
    """  
    identified_labels = {}  
    
##############	ADD YOUR CODE HERE	##############
    for img_index, label in zip(range(5), detected_list):
            identified_labels[chr(ord('A') + img_index)] = label.lower()
##################################################
    return identified_labels


###############	Main Function	#################
if __name__ == "__main__":
        try:
            task_4a_return()
        except KeyboardInterrupt:
            print('Interrupted')
            # if os.path.exists('arena.png'):
             # os.remove('arena.png')
            if os.path.exists('detected_events.txt'):
                os.remove('detected_events.txt')
            sys.exit()
    