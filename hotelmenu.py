#simple project to manage hotel menu

menu = {
    'Pizza': 10.9,
    'Burger': 8.5,
    'Pasta': 12.0,
    'Salad': 7.5,
    'Soda': 2.5,
    'Water': 1.5,
    'Coffee': 3.0,
    'Tea': 2.0,
    'Juice': 2.5,
}

print("Welcome to the Hotel Menu!")
print("Here is the menu:")
print("Pizza: 10.9 SAR\nBurger: 8.5 SAR\nPasta: 12.0 SAR\nSalad: 7.5 SAR\nSoda: 2.5 SAR\nWater: 1.5 SAR\nCoffee: 3.0 SAR\nTea: 2.0 SAR\nJuice: 2.5 SAR")

order_total = 0

item_1 = input("Enter the name of item you want to order = ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.") 
else:
    print(f"Ordered item {item_1} is not available in the menu.")

another_order = input("Do you want to add another item to your order? (yes/no) = ")
if another_order.lower() == 'yes':
    item_2 = input("Enter the name of item you want to order = ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available in the menu.")

print(f"The total amount of items to pay is {order_total} SAR.")