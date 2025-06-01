user_number = int(input("Enter a number: "));

def even_or_odd(number):
    if number % 2 == 0:
        print("The number you entered is even.");
    else:
        print("The number you entered is odd.");

even_or_odd(user_number);