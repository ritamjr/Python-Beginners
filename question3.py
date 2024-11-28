# Write a program to calculate the total expenses. Quantity and price per item are input by the user and discount of 10% is offered if the expense is more than 5000.
quantity =int(input("Enter the Quantity: "))
price = float(input("Enter the price: "))

expenses =quantity * price
print(expenses)

if expenses >=5000 :
    print("Discount = 10%")
    print(expenses-(expenses*0.1))
