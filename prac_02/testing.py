import random


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def return_multiple(a, b):
    return a, b


print(return_multiple("a", "b"))


def print_line(length):  # void function
    print("-" * length)

def print_line2(length=20, pen='*'):
    print(pen * length)

def main():
    height = random.uniform(1, 2)
    print(height)
    if calculate_bmi(height, 99) < 15:
        print("Not considered overweight")

    print_line(5)
    print_line2()#default parameter

    name ="a"
    print("Hello", name, "!", sep="", end=" ") # sep = things in comma, end => end var


#unpacking variables

def format_date(day,month,year):
    return f"{day}/{month}/{year}"
date = (22, 11, 1988) # this is a tuple
format_date(16, 11, 1988)  # * unpacks date tuple, for tuple need upack
format_date(16, 'May', 1970)  # error: month & year unfilled


set1 ={'a','b'}
set1.add('a')
print("cccc")
print(set1)

main()
