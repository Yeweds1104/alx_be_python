monthly_income = input("Enter your monthly income: ");
monthly_expenses = input("Enter your total monthly expenses: ");
monthly_savings = int(monthly_income) - int(monthly_expenses);
interest = 0.05;
projected_saving = monthly_savings * 12 + monthly_savings * 12 * interest;
print("Your monthly savings are $", monthly_savings);
print("Projected savings after one year, with interest, is: $", projected_saving);