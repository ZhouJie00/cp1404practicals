from random import randint

all_shown_numbers = []
for i in range(int(input("How many quick picks? "))):
    for _ in range(6):

        random_number = ""
        sub_loop_switch = True

        while sub_loop_switch:
            random_number = randint(1,45)
            if random_number not in all_shown_numbers:
                all_shown_numbers.append(random_number)
                sub_loop_switch = False
        print(str(random_number).rjust(2), end=" ")
    print()

"""
How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
 """