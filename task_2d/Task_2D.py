'''
*****************************************************************************************
*
*        		===============================================
*           		GeoGuide(GG) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 2D of GeoGuide(GG) Theme (eYRC 2023-24).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''
############################## FILL THE MANDATORY INFORMATION BELOW ###############################

# Team ID:			[ GG_2651 ]
# Author List:		[ Rebba.Gurupriya, Vikas Tiwari, Renukesh K, Vandhana S ]
# Filename:			Task_2D.py
# Functions:	    [ read_csv, write_csv, tracking, lat_lon ]
###################################################################################################

# IMPORTS (DO NOT CHANGE/REMOVE THESE IMPORTS)
import csv
import time

# Additional Imports
'''
You can import your required libraries here

'''

# DECLARING VARIABLES (DO NOT CHANGE/REMOVE THESE VARIABLES)
path1 = [11, 14, 13, 18, 19, 20, 23, 21, 22, 33, 30, 35, 32, 31, 34, 40, 36, 38, 37, 39, 41, 50, 4, 6, 52, 7, 8, 1, 2, 11]
path2 = [11, 14, 13, 10, 9, 51, 53, 0, 39, 37, 38, 28, 25, 54, 5, 3, 19, 20, 17, 12, 15, 16, 27, 26, 24, 29, 40, 34, 31, 32, 35, 30, 33, 22, 21, 23, 20, 19, 18, 13, 14, 11]
###################################################################################################

# Declaring Variables
'''
You can delare the necessary variables here

'''
lat_lon = {}

def read_csv(csv_name):
    # open csv file (lat_lon.csv)
    # read "lat_lon.csv" file 
    # store csv data in lat_lon dictionary as {id:[lat, lon].....}
    # return lat_lon
    with open(csv_name, mode="r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        #next(reader)  # Skip the header row

        # Iterate through rows and store data in lat_lon dictionary
        for row in reader:
            id = (row[0])  
            lat = (row[1])  
            lon = (row[2])  

            lat_lon[id] = [lat, lon]  
    return lat_lon 

def write_csv(loc, csv_name):

    # open csv (csv_name)
    # write column names "lat", "lon"
    # write loc ([lat, lon]) in respective columns
        # open csv (csv_name)
      # Open CSV file and write location data
    with open(csv_name, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['lat', 'lon'])  # Write header row
        writer.writerow(loc)  # Write location data


def tracker(ar_id, lat_lon):

    # find the lat, lon associated with ar_id (aruco id)
    # write these lat, lon to "live_data.csv"

 # Check if the ar_id exists in the lat_lon dictionary
    if str(ar_id) in lat_lon:
        # Get latitude and longitude values corresponding to the ar_id
        lat, lon = lat_lon[str(ar_id)]
        
        # Write the lat and lon values to "live_data.csv" file
        with open('live_data.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['lat', 'lon'])  # Write header row
            writer.writerow([lat, lon])  # Write lat and lon values
    coordinate = [lat,lon]
    return coordinate 

# ADDITIONAL FUNCTIONS

'''
If there are any additonal functions that you're using, you shall add them here. 

'''

###################################################################################################
########################### DO NOT MAKE ANY CHANGES IN THE SCRIPT BELOW ###########################

def main():
    ###### reading csv ##############
    lat_lon = read_csv('lat_long.csv')
    print("###############################################")
    print(f"Received lat, lons : {len(lat_lon)}")
    if len(lat_lon) != 48:
        print(f"Incomplete coordinates received.")
        print("###############################################")
        exit()
    ###### Test case 1 ##############
    print("########## Executing first test case ##########")
    start = time.time()
    passed = 0
    traversedPath1 = []
    for i in path1:
        t_point = tracker(i, lat_lon)
        traversedPath1.append(t_point)
        time.sleep(0.5)
    end = time.time()
    if None in traversedPath1:
        print(f"Incorrect path travelled.")
        exit()
    print(f"{len(traversedPath1)} points traversed out of {len(path1)} points")
    print(f"Time taken: {int(end-start)} sec")
    if len(traversedPath1) != len(path1):
        print("Test case 1 failed. Travelled path is incomplete")
    else:
        print("Test case 1 passed !!!")
        passed = passed+1
    print("########## Executing second test case ##########")
    ###### Test case 2 ##############
    start = time.time()
    traversedPath2 = []
    for i in path2:
        t_point = tracker(i, lat_lon)
        traversedPath2.append(t_point)
        time.sleep(0.5)
    end = time.time()
    if None in traversedPath2:
        print(f"Incorrect path travelled.")
        exit()
    print(f"{len(traversedPath2)} points traversed out of {len(path2)} points")
    print(f"Time taken: {int(end-start)} sec")
    if len(traversedPath2) != len(path2):
        print("Test case 2 failed. Travelled path is incomplete")
    else:
        print("Test case 2 passed !!!")
        passed = passed+1
    print("###############################################")
    if passed==0:
        print("0 Test cases passed please check your code.")
    elif passed==1:
        print("Partialy correct, look for any logical erro ;(")
    else:
        print("Congratulations!")
        print("You've succesfully passed all the test cases \U0001f600")
    print("###############################################")
if __name__ == "__main__":
    main()
