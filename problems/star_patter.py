'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Vikas Tiwari , Renukesh
# Filename:         generate_pattern.py
# Functions:        generate_pattern, main
# Global variables: None
'''

# Function to generate the star and hash pattern for a given N


def generate_pattern(N):
    '''
    Purpose:
    ---
    Generates a pattern of stars and hashes for a given value N.

    Input Arguments:
    ---
    `N` :  [ int ]
        The input value for which the pattern is generated.

    Returns:
    ---
    None

    Example call:
    ---
    generate_pattern(5)
    '''
    for i in range(N):
        stars = N - i  # Number of stars in this row
        hashes = (N - stars) // 5  # Number of hashes in this row

        # Print stars and hashes in the current row
        for j in range(stars):
            if j % 5 == 4:
                print("#", end="")
            else:
                print("*", end="")
        print()  # Move to the next line after printing the row


def main():
    '''
    Purpose:
    ---
    Reads the number of test cases, processes each test case, and generates the pattern.

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
    # Read the number of test cases
    test_cases = int(input())

    # Process each test case
    for _ in range(test_cases):
        # Read the value of N for this test case
        N = int(input())

        # Generate and print the pattern for the current test case
        generate_pattern(N)


if __name__ == '__main__':
    main()
