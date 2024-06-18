from math import sqrt
print("Welcome to our program")
print ("This program will help you to find the square root of a number")
print ("Please enter a number")

number1 = int (input())

def sqrRootnum(number1):
    return sqrt(number1)

if number1>=0:
    resultOfSqrt= sqrRootnum(number1)
    print("The square root of your number is:")
    print (resultOfSqrt)
else: 
    print("Please enter a number higher than zero")




