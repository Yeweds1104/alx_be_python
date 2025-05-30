number = int(input("Enter a number to see its multiplication table: "));
for mul in range(1,11):
    result = number * mul;
    print(number, " * ", mul, " = ", result);