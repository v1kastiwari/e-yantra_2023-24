'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Vikad Tiwari
# Filename:         compute_values.py
# Functions:        compute_values, main
# Global variables: None
'''

def compute_values(n):
    '''
    Purpose:
    ---
    Computes the desired values for a single test case based on the given input n.
    
    Input Arguments:
    ---
    `n` :  [ int ]
        The input value for which values need to be computed.
    
    Returns:
    ---
    `result` :  [ list of int ]
        A list containing the computed values.
    
    Example call:
    ---
    compute_values(5)
    '''
    result = []
    for i in range(n):
        if i == 0:
            result.append(3)
        elif i % 2 == 0:
            result.append(2 * i)
        else:
            result.append(i ** 2)
    return result

def main():
    '''
    Purpose:
    ---
    Reads the number of test cases, computes values for each test case, and prints the results.
    
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
        n = int(input())  # Input for each test case
        values = compute_values(n)
        # Print the computed values without spaces after the last integer
        print(*values)

if __name__ == "__main__":
    main()
