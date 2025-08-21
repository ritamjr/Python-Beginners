# Concession Stand Program

menu = {"Pizza": 400,
        "Nachos": 180,
        "Popcorn": 600,
        "Fries": 120,
        "Pasta": 180,
        "Chips": 50,
        "Soda": 100,
        "Diet_Coke": 150}

cart = []
total = 0

print("--------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: Rs{value:.2f}")
print("-----------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not available. Please choose from the menu.")

print("--------ORDER----------")
for item in cart:
    total += menu[item]
    print(f"{item:10}: Rs{menu[item]:.2f}")

print("-----------------------")
print(f"Total is: Rs{total:.2f}")
