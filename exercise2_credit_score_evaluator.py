#input for checker

score = int(input("What's your credit score? "))

#check for valid score range
if score < 300 or score > 850:
    print("invalid score.")
elif score >= 750:
    print("Excellent - Loan approved. Interest rate: Low")
elif 700<= score < 750:
    print("Good - Loan Approved with Review. Interest rate: Low")
elif 600 <= score < 700:
    print("Fair - Loan Conditional. Seek credit improvement.")
else: # score < 600
    print("Poor - Loan Denied. Seek credit counseling.")

