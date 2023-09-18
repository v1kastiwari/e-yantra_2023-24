# Function to perform the operations on the list
def perform_operations(L,N):
    # 1. Print the list in reverse order
    reverse_list = L[::-1]
    print(" ".join(map(str, reverse_list)))

    # 2. Print every 3rd number with 3 added to it
    for i in range(0, N, 3):
        if i < len(L):
            print(L[i] + 3, end=" ")

    # 3. Print every 5th number with 7 subtracted from it
    for i in range(0, N, 5):
        if i < len(L):
            print(L[i] - 7, end=" ")

    # 4. Sum of all numbers with an index between 3 and 7 (inclusive)
    index_sum = sum(L[3:8])
    print(index_sum)

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the length of the list
    N = int(input())
    
    # Input the list of numbers
    L = list(map(int, input().split()))
    
    # Perform the required operations
    perform_operations(L,N)
