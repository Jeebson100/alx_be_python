monthly_income = int(input("enter your monthly_income"))
monthly_expenses = int(input("enter your total monthly_expenses"))
monthly_savings = monthly_income - monthly_expenses
print(f"your monthly savings are $ {monthly_savings}. ")
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 * (1 + annual_interest_rate)
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")