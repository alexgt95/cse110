"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Professor: Sister Creer
Project: Shopping Cart
Creativity Credit Explanation: I learned about dictionaries and nested dictionaries from https://www.w3schools.com/python/python_dictionaries_nested.asp
,https://stackoverflow.com/questions/50570781/shopping-cart-total-price-in-nested-dict-python, and got some ideas from further ahead in the course.
I made a list of dictionaries to add an amount of items to the cart and addded the total price into the "display_cart" function.
"""

def add_item(cart):
    name = input("Enter item name: ").lower()
    try:
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))
        cart.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print(f"{quantity} x {name} added to the cart.")
    except ValueError:
        print("Invalid price or quantity.")

def display_cart(cart):
    if not cart:
        print("Cart is empty.")
        return
    total = 0
    print("\nCart Contents:")
    for idx, item in enumerate(cart, start=1):
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{idx}. {item['name'].title()} - ${item['price']:.2f} x {item['quantity']} = ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")

def remove_item(cart):
    if not cart:
        print("Cart is empty.")
        return
    display_cart(cart)
    try:
        idx = int(input("Enter the index of the item to remove: "))
        if 1 <= idx <= len(cart):
            removed = cart.pop(idx - 1)
            print(f"{removed['name']} removed.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def compute_total(cart):
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
    print(f"Total: ${total:.2f}")

def main():
    cart = []
    while True:
        print("\nShopping Cart Menu:")
        print("\n1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            remove_item(cart)
        elif choice == "4":
            compute_total(cart)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
