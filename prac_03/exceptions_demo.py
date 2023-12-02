"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# when an object is assigned with a wrong value, e.g. int() doesn't allow a string to be its argument

2. When will a ZeroDivisionError occur?
# when a value is divided by 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# introduce a try and except statement, include ZeroDivisionError in the except parameter
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")