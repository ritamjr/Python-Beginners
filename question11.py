'''
Any character is entered by the user; write a program to determine whether the character entered is a capital letter, a small case letter, a digit or a special symbol. The following table shows the range of ASCII values for various characters.

'''
char=input("enter charecter: ")
if len(char)==1:
    a=ord(char)
    if a>=65 and a<=90:
        print("Capital")
    elif a>=97 and a<=122:
        print("Small")
    elif a>=48 and a<=57:
        print("Digit")
    else:
        print("Symbol")
else:
    print("enter a single charecter")