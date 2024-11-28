'''
The marks obtained by a student in 5 different subjects are input by the user. The student gets a division as per the following rules:
Percentage above or equal to 60 - First division 
Percentage between 50 and 59 - Second division 
Percentage between 40 and 49 - Third division 
Percentage less than 40 - Fail 
Write a program to calculate the division obtained by the student.

'''
Math=float(input("Enter the marks of Math: "))
Computer=float(input("Enter the marks of Computer: "))
English=float(input("Enter the marks of English: "))
Hindi=float(input("Enter the marks of Hindi: "))
Bengali=float(input("Enter the marks of Bengali: "))


tot = Math + Computer + English + Hindi + Bengali
p = (tot/500) * 100

print("Total Marks: ",tot)
print("Percentage: ",p)

if p>= 60 :
    print("First Division")
elif p <= 50 and p>=59 :
    print("Second Diviion")
elif p <=40 and p>=49 :
    print("Third Division")
else :
    print("Fail")


