#creating prompts for user input

revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

#calculating profit
profit = revenue - cost

#checking for valid revenue before calculating margin
if revenue > 0:
    margin = (profit / revenue) * 100
    #print formatted results
    print(f"Profit: ${profit:.2f}")
    print(f"Margin: {margin:.2f}%")
else:
    print("Revenue must be greater than zero to calculate margin.")