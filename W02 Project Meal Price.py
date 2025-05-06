"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Project Meal Price
Creativity Credit Explanation: I added an if statement at the end 
to determine whether the customer paid enough money to cover the total price.
"""

#Request information from the customer
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_meal_count = int(input("How many children's meals do you want? "))
adult_meal_count = int(input("How many adult's meals do you want? "))
subtotal = (child_meal * child_meal_count) + (adult_meal * adult_meal_count)

#Display the subtotal
print(f"Subtotal: ${subtotal:.2f}")
#Request the tax rate, calculate it, and display it
tax_rate = int(input("What is the tax rate? "))
tax = subtotal * (tax_rate / 100)
print(f"Sales Tax: ${tax:.2f}")
#Display the total
total = subtotal + tax
print(f"Total: ${total:.2f}")
#Request the payment amount, determine if it is enough, and display the change if it was enough
payment = float(input("What is the payment amount? "))
if payment < total:
    print("Not enough money")
else:
    change = payment - total
    print(f"Change: ${change:.2f}")