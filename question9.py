'''
Write a program to calculate the monthly telephone bills as per the following rule: 
Minimum Rs. 200 for upto 100 calls. 
Plus Rs. 0.60 per call for next 50 calls. 
Plus Rs. 0.50 per call for next 50 calls. 
Plus Rs. 0.40 per call for any call beyond 200 calls.

'''
call=int(input("Enter call: "))
if call<=100:
    bill=200
elif call<=150:
    bill=200+(call-100)*0.60
elif call<=200:
    bill=200+50*0.60+(call-150)*0.50
else:
    bill=200+50*0.60+50*0.50+(call-200)*0.40

print("No of calls: ",call)
print("Bill: ",bill)