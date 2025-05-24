income = input("Enter your monthly income: ");
expense = input("Enter your total monthly expenses: ");
saving = int(income) - int(expense);
interest = 0.05;
annual_saving = saving * 12 + saving * 12 * interest;
print("Your monthly savings are $", saving);
print("Projected savings after one year, with interest, is: $", annual_saving);