'''
# Team ID:          gg_2651
# Theme:            GeoGuid
# Author List:      Rebba Gurupriya , S Vandana 
# Filename:         inventory_management.py
# Functions:        add_item, delete_item, main
# Global variables: inventory
'''

# Function to perform ADD operation
def add_item(item_name, quantity):
    '''
    Purpose:
    ---
    Adds an item to the inventory or updates its quantity.
    
    Input Arguments:
    ---
    `item_name` :  [ str ]
        The name of the item to be added or updated.
    
    `quantity` :  [ int ]
        The quantity of the item to be added or updated.
    
    Returns:
    ---
    None
    
    Example call:
    ---
    add_item("apple", 5)
    '''
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
    else:
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")

# Function to perform DELETE operation
def delete_item(item_name, quantity):
    '''
    Purpose:
    ---
    Deletes a specified quantity of an item from the inventory.
    
    Input Arguments:
    ---
    `item_name` :  [ str ]
        The name of the item to be deleted.
    
    `quantity` :  [ int ]
        The quantity of the item to be deleted.
    
    Returns:
    ---
    None
    
    Example call:
    ---
    delete_item("apple", 2)
    '''
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"DELETED Item {item_name}")
        else:
            print(f"Item {item_name} could not be DELETED")
    else:
        print(f"Item {item_name} does not exist")

def main():
    '''
    Purpose:
    ---
    Reads input, performs inventory operations, and calculates the total quantity.
    
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
    # Number of test cases
    T = int(input())

    for _ in range(T):

        # Number of items in the lab initially
        N = int(input())

        # Populate the initial inventory
        for _ in range(N):
            item_name, item_quantity = input().split()
            inventory[item_name] = int(item_quantity)

        # Number of operations to be performed
        M = int(input())

        # Perform operations
        for _ in range(M):
            operation, item_name, quantity = input().split()
            quantity = int(quantity)

            if operation == "ADD":
                add_item(item_name, quantity)
            elif operation == "DELETE":
                delete_item(item_name, quantity)

        # Calculate and print the sum of quantities in the inventory
        total_quantity = sum(inventory.values())
        print("Total Items in Inventory:")
        print(total_quantity)

# Initialize the inventory dictionary
inventory = {}
if __name__ == '__main__':
    main()
