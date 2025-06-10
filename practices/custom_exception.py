class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return f"Sorry, the number '{self.number}' is too high!"

try:
    num = int(input("Enter a number upto 100: "))
    if num < 100:
        print(f"You entered proper number {num}.")
    else:
        raise ValueTooHighError(num)
except ValueError:
    print("You are not entered a number.")
finally:
    print("Program ends...")