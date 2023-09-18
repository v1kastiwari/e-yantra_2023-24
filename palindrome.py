'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Vikas Tiwari 
# Filename:         palindrome.py
# Functions:        palindrome, main
# Global variables: None
'''

def palindrome(s):
    '''
    Purpose:
    ---
    Checks if the given string is a palindrome.
    
    Input Arguments:
    ---
    `s` :  [ str ]
        The input string to be checked for palindrome.
    
    Returns:
    ---
    `True` :  [ bool ]
        If the input string is a palindrome.
    
    `False` :  [ bool ]
        If the input string is not a palindrome.

    Example call:
    ---
    palindrome("A man, a plan, a canal: Panama")
    '''
    s = s.lower()  # Converts all characters into lowercase
    # Filters the alphanumeric characters in the string and joins them
    s = ''.join(filter(str.isalnum, s))
    # Checks if the string and its reverse are equal (returns True or False)
    return s == s[::-1]

def main():
    '''
    Purpose:
    ---
    Reads the number of test cases, checks if each input string is a palindrome,
    and prints the result.

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
    test_cases = int(input())
    for _ in range(test_cases):
        s = input()
        if palindrome(s):
            print('It is a palindrome')
        else:
            print('It is not a palindrome')

if __name__ == '__main__':
    main()