"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


sales = 1
while sales>=0:
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        print(f"User received 10% discount, Total: {(sales*0.1):.0f}")
    elif sales >= 1000:
        print(f"User received 10% discount, Total: {(sales*0.15):.0f}")