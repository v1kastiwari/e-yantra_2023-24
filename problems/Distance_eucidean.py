'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Vikas Tiwari , Renukesh
# Filename:         calculate_distance.py
# Functions:        compute_distance, main
# Global variables: None
'''

# Import the required module
import math


def compute_distance(x1, y1, x2, y2):
    '''
    Purpose:
    ---
    Calculates the Euclidean distance between two points given their coordinates.

    Input Arguments:
    ---
    `x1` :  [ int ]
        x-coordinate of the first point.

    `y1` :  [ int ]
        y-coordinate of the first point.

    `x2` :  [ int ]
        x-coordinate of the second point.

    `y2` :  [ int ]
        y-coordinate of the second point.

    Returns:
    ---
    None

    Example call:
    ---
    compute_distance(1, 2, 4, 6)
    '''
    # Calculate the Euclidean distance
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Print the distance value with precision up to 2 decimal places
    print(f"Distance: {distance:.2f}")


def main():
    '''
    Purpose:
    ---
    Reads the number of test cases, computes the Euclidean distance for each case, and prints the results.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    Called automatically when the script is executed.
    '''
    # Take the T (test_cases) input
    test_cases = int(input())

    # Iterate through each test case
    for _ in range(test_cases):
        # Read the input coordinates for two points
        x1, y1, x2, y2 = map(int, input().split())
        # Calculate and print the Euclidean distance
        compute_distance(x1, y1, x2, y2)


if __name__ == '__main__':
    main()
