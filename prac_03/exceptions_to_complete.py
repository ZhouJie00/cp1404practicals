"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
result = ""
is_finished = False  # while true/false can be used because there are no conditions on the previous line
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)