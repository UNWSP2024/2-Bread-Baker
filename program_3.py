# Name: Ariana Fafach
# Date: 1/21/2026
# Title: Program #3: Total Purchase

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    # Get user input
    Price_1 = float(input("Enter the price of the first item: "))
    Price_2 = float(input("Enter the price of the second item: "))
    Price_3 = float(input("Enter the price of the third item: "))
    Price_4 = float(input("Enter the price of the fourth item: "))
    Price_5 = float(input("Enter the price of the fifth item: "))
    
    # Calculate subtotal
    Subtotal = Price_1 + Price_2 + Price_3 + Price_4 + Price_5

    #Calculate amount of sales tax
    Sales_tax = Subtotal * 0.07

    #Calculate total
    Total = Subtotal + Sales_tax

    #Display values with dollar signs and precision to two decimal places
    #Also put in commas for large numbers
    print(f"Your subtotal is: ${Subtotal:,.2f}")
    print(f"The amount of sales tax is: ${Sales_tax:,.2f}")
    print(f"Your total is: ${Total:,.2f}")

calculate_total_purchase()