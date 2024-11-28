'''In a company an employee is paid as under: 
If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary 
and DA = 90% of basic salary.
If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 
and DA = 98% of basic salary. 
If the employee's salary is input by the user write a program to find his gross salary. '''


bs=int(input("Enter basic salary: "))
if(bs<1500):
    hr=bs*0.1
    da=bs*0.9
elif bs>=1500:
    hr=500
    da=bs*0.98

gs=bs+hr+da
print("basic salary: ",bs)
print("HRA: ",hr)
print("DA: ",da)
print("Gross salary: ",gs)