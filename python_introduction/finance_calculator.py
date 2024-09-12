monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses 
simple_annual_interest = 0.05
Projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest))
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")
