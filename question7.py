'''Any year is input by the user. 
Write a program to determine whether the year is a leap year or not'''

year = int(input("Enter the Year: "))

if year%4==0 :
    print("Leap Year")
else :
    print("Not a Leap Year")
