#Tax Bracket Calculator

def get_tax_bracket(income):
    if income < 0:
        return "Invalid income"
    elif income < 50000:
        bracket = "low (10%)"
        rate = 0.10
    elif 50000 <= income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:  # income >= 100000
        bracket = "High (30%)"
        rate = 0.30
    
#Bonus: ternary expression for deduction eligibility
    bracket = bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket

    return bracket, rate

#Main program

income = float(input("What is your annual income? "))

bracket_info = get_tax_bracket(income)

if bracket_info == "Invalid income.":
    print (bracket_info)
else:
    bracket, rate = bracket_info
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: ${estimated_tax:.2f}")
