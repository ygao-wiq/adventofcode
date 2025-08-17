# repayment.py

# Home loan parameters
principal = 390000         # Total obligation (loan amount)
annual_interest_rate = 2.85  # Annual interest rate in percent
monthly_installment = 3460   # Monthly repayment amount

# Convert annual interest rate to monthly decimal
monthly_interest_rate = annual_interest_rate / 100 / 12

# Initialize variables
remaining_principal = principal
month = 0
total_interest_paid = 0.0

print(f"{'Month':<6} {'Payment':<10} {'Interest':<10} {'Principal':<10} {'Remaining':<12}")

for i in range(1, 97):  # Arbitrary large number to ensure we cover all months
    month += 1
    interest = remaining_principal * monthly_interest_rate
    principal_paid = min(monthly_installment - interest, remaining_principal)
    payment = interest + principal_paid
    remaining_principal -= principal_paid
    total_interest_paid += interest

    print(f"{month:<6} {payment:<10.2f} {interest:<10.2f} {principal_paid:<10.2f} {remaining_principal:<12.2f}")

    if remaining_principal <= 0:
        break

print(f"\nTotal months: {month}")
print(f"Total interest paid: {total_interest_paid:.2f}")
print(f"Total payment: {month * monthly_installment:.2f}")