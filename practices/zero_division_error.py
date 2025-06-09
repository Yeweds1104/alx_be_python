num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print("The division is performed!")
finally:
    print("Finally is executed!")
    