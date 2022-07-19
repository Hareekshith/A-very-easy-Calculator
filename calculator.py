x = int(input("Enter the first num: "))
z = 1

operationmode = int(input("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponent
7. Factorial
The operation mode you'd like to choose now: 
"""))
if(operationmode == 7):
    for i in range(x):
        z = z*(i+1)
    print(z)
elif(operationmode == 1 or 2 or 3 or 4 or 5 or 6):
    y = int(input("Enter the second num: "))
else:
    print("GULUGULU, ERROR")

if (operationmode == 1):
    print("The result is: ", x+y)
elif (operationmode == 2):
    print("The result is: ", x-y)
elif (operationmode == 3):
    print("The result is: ", x*y)
elif (operationmode == 4):
    print("The result is: ", x/y)
elif (operationmode == 5):
    print("The result is: ", x%y)
elif (operationmode == 6):
    print("The result is: ", x**y)

## program successfully completed 