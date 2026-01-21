# Name: Ariana Fafach
# Date: 1/21/2026
# Title: Program #2: Average Age

def average_age():
    # Get User Input
    Friend1 = float(input("Enter the age of your first friend: "))
    Friend2 = float(input("Enter the age of your second friend: "))
    Friend3 = float(input("Enter the age of your third friend: "))
    Friend4 = float(input("Enter the age of your fourth friend: "))
    Friend5 = float(input("Enter the age of your fifth friend: "))

    # Sum ages1
    Sum_of_ages = Friend1 + Friend2 + Friend3 + Friend4 + Friend5
 
    # Average the ages
    Average_age = (Sum_of_ages)/5

    # Print the results
    print("The average age of your five friends is:", Average_age)

# Line which calls the above function.
average_age()