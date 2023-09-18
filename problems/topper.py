# cook your dish here
'''
# Team ID: gg_2651
# Theme: GeoGuide
# Author List: Renukesh.K,Vikas Tiwari
# Filename: find toppers.py
# Functions: process_testcase,main  
# Global variables: None
'''
# Function to process each testcase
def process_testcase():
    '''
    Purpose:
    ---
    Finds the students with maximum score and prints 
    his/her name. If there is a tie, names is printed
    in ascending alphabetical order.

    Input Arguments:
    ---
    'N' : [int]
        The input is for number of students in the test case  
        
  Returns:
  ---
  None

  Example call:
  ---
  N=3
  students=[("Sam",40.8),("Riya",30.7),("Harry",41)]
    '''
  # purpose:
   # finds 
    N = int(input())  # Number of students in this testcase
    students = []  # List to store student names and scores

    # Read student names and scores for this testcase
    for _ in range(N):
        name, score = input().split()
        score = float(score)
        students.append((name, score))

    # Find the maximum score
    max_score = max(student[1] for student in students)

    # Filter students with the maximum score
    max_score_students = [student[0] for student in students if student[1] == max_score]

    # Sort the names in ascending alphabetical order
    max_score_students.sort()

    # Print the names
    for name in max_score_students:
        print(name)

# Main function
if __name__ == "__main__":  # Use double underscores for __name__ and "__main__"
    '''
    Purpose:
    ---
    Asks the user to input the number of test cases and calls 
    the function process_testcase().

    Input Arguments:
    ---
    'T' : [int]
        The input value is for number of testcases.

        Returns:
        ---
        None

        Example call:
        ---
          T=1
    '''
    T = int(input())  # Number of testcases
    for _ in range(T):
        process_testcase()
