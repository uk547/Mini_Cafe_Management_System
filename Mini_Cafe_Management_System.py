menu = {
    "Pizza": 100,
    "Burger": 50,
    "Pasta": 80,
    "Salad": 90,
    "Soda": 30,
    "Water": 20,
}
#ask for the customer"s name
customer_name = input("Please enter your name: ")
# Display a welcome message
print(f"Welcome {customer_name} to Khullar's restaurant!")
# Display the menu
print("Here is the menu:\nPizza:100, \nBurger:50, \nPasta:80, \nSalad:90, \nSoda:30, \nWater:20")
order_total = 0
item_1 = input("Enter the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order.")
while item_1.lower() != 'done':
    item_1 = input("Enter the next item you want to order (or type 'done' to finish) = ")
    if item_1.lower() == 'done':
        break
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"{item_1} added to your order.")
    else:
        print(f"Sorry, {item_1} is not on the menu.")
# Display the total amount
print(f"Thank you for your order, {customer_name}! Your total is: {order_total} rupees.")