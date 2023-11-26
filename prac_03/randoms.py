import random

# Python has a number of random functions
# - contained within the random module.
# Unlike the built-in functions (print(), input(), etc.)
# the random functions are not built-in but need to be imported.
# Modules are reusable collections of functions,
# classes and variables (constants) related to a specific topic
# (e.g., maths, operating system services, handling dates and times).
# Python has a useful built-in function for finding out about the local scope
# of something, called dir().


print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# 15

# What was the smallest number you could have seen, what was the largest?
# smallest = 5, largest = 20

print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# 7

# What was the smallest number you could have seen, what was the largest?
# smallest = 3, largest = 10

# Could line 2 have produced a 4?
# No

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# 2.7155677423456694

# What was the smallest number you could have seen, what was the largest?
# smallest = 2.5, largest = 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
