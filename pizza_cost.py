#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 4, 2025
# This program asks the user for the size of a pizza,
# which is provided through the value of the diameter in inches.
# Using the size, the program calculates and displays the cost of the pizza
import constants


def main():
    # Get the Pizza's diameter in inches
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # Calculate the subtotal
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST
    subtotal += constants.INGREDIENT_COST_PER_INCH * diameter
    # Calculate the tax
    tax = subtotal * constants.HST
    # Calculate the total
    total = subtotal + tax

    # Display the total cost of the pizza to the user
    print(f"The total cost is ${total:,.2f}")


if __name__ == "__main__":
    main()
