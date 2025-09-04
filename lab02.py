"""
Author: Ernest Friday
Date: 08/09/2025
Assignment:  Lab 02
Course:  CPSC 1051
Lab Section: 002

This program will ask the user for how many chips, sandwiches, and pounds of bannanas they want, then calculate the total cost before tax, display it, ask for tax rate, then calculate and display the total cost after tax.

"""

print("Welcome to the Clemson Market!")

print("We have the following items available:")
print("Bag of Chips: $5.99 each")
print("Turkey Sandwich: $13.23 each")
print("Bananas: $2.73 per lb")

cost_of_chips = float(5.99)
cost_of_turkey = float(13.23)
cost_of_nanners = float(2.73)



print("How many bags of chips do you want?")
number_of_chips = int(input())
print("How many turkey sandwiches do you want?")
number_of_turkey = int(input())
print("How many lbs of bananas do you want?")
lbs_of_nanners =  int(input())

total_before_tax = ((number_of_chips * cost_of_chips)+(number_of_turkey * cost_of_turkey)+(lbs_of_nanners * cost_of_nanners))


print(f"Your total before tax is ${total_before_tax:.2f}")

print("Please enter the tax rate:")
tax_rate = float(input())

total_after_tax = total_before_tax + total_before_tax * (tax_rate/100)

print(f"Your total after tax is ${total_after_tax:.2f}. Thank you for shopping at the Clemson Market!")