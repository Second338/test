# Savings Account Monthly Balance Calculator
# Initial deposit: $7000, Annual interest rate: 6%

initial_deposit = 70000
annual_rate = 0.1
monthly_rate = annual_rate / 12
balance = initial_deposit
months = 48

print("Monthly Balance Summary")
print("=" * 45)
print(f"{'Month':<8} {'Balance':>15}")
print("=" * 45)

for month in range(1, months + 1):
    balance = balance * (1 + monthly_rate)
    print(f"{month:<8} ${balance:>14,.2f}")

print("=" * 45)
print(f"\nFinal Balance after 48 months: ${balance:,.2f}")
print(f"Total Interest Earned: ${balance - initial_deposit:,.2f}")
