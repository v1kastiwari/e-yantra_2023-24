'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Vikas Tiwari , Renukesh
# Filename:         word_length_counter.py
# Functions:        count_word_lengths, main
# Global variables: None
'''

# Function to count and print the length of each word in a string
def count_word_lengths(s):
    '''
    Purpose:
    ---
    Counts and prints the length of each word in a string, separated by commas.
    
    Input Arguments:
    ---
    `s` :  [ str ]
        The input string containing words.
    
    Returns:
    ---
    None
    
    Example call:
    ---
    count_word_lengths("Hello world")
    '''
    words = s.split()  # Split the input string into words
    lengths = [len(word) for word in words]  # Calculate the length of each word
    result = ','.join(map(str, lengths))  # Convert lengths to a comma-separated string
    print(result)

def main():
    '''
    Purpose:
    ---
    Reads the number of test cases, processes each test case, and counts word lengths.
    
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
    # Input the number of test cases
    T = int(input())

    # Process each test case
    for _ in range(T):
        input_string = input()
    
        # Check if the input string starts with "@" as mentioned in the problem statement
        if input_string.startswith("@"):
            input_string = input_string[1:]  # Remove the "@" symbol at the beginning
            count_word_lengths(input_string)  # Call the function to count and print word lengths

if __name__ == '__main__':
    main()
