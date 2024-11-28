#Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered by the user. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
print("Enter the Angles of the Triangle: ")
sum =0
for i in range(3):
    angle=int(input("Enter the angles: "))
    sum += angle
if sum == 180 :
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")