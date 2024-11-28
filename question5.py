# If the ages of Ram, Sulabh and Ajay are input by the user, write a program to determine the youngest of the three.

r =int(input("Enter the age of Ram: "))
s =int(input("Enter the age of Saulabh: "))
a =int(input("Enter the age if Ajay: "))

if r<s and r<a :
    print("Ram is youngest")
elif s<r and s<a :
    print("Saulabh is Youngest")
else :
    print("Ajay is Youngesr")