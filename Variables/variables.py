from math import sqrt, log, pi
#'''
number1 = float(input("Enter first number: \n"))
number2 = float(input("Enter second number: \n"))
operation = input("(+) for add, (-)for sub, (*) for mult, (/) for division, (%) for remainder only, (//) for no reminder:\n")

if(operation == "+"):
    result = number1 + number2
elif(operation == "-"):
    result = number1 - number2
elif(operation == "*"):
    result = number1 * number2
elif(operation == "/"):
    if (number2 == 0):
        result= "0 is not valid for division"
    else:
        result = number1 / number2
elif(operation == "%"):
    if (number2 == 0):
        result = "0 is not valid for division"
    else:
        result = number1 % number2
elif(operation == "//"):
    if (number2 == 0):
        print("0 is not valid for division")
    else:
        result = number1 // number2
else: result = "invalid operation"
print(result)
#'''