#Write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred. Cost price and selling price of an item is input by the user

cp =float(input("Enter the Cost Price: "))
sp = float(input("Enter the Selling Price: "))

Loss = cp - sp
Profit = sp - cp

if cp>sp :
    print("Loss", Loss)
else :
    print("Profit", Profit)

