# import random
#
# name = "tom"
#
# # try:
# #     int(name)
# #
# # except ValueError as ex:
# #     print(ex)
# #
#
#
# # try:
# #     int(name)
# #
# # except Exception as ex:
# #     print(ex)
#
# FILENAME = "secret.txt"
#
#
# def main():
#     secret = load_number(FILENAME)
#     guess = get_valid_number()
#
#     while guess != secret:
#         print("Guess again!")
#         guess = get_valid_number()
#     print("You got it!")
#
#
# def get_valid_number():
#     is_valid_input = False
#     guess = ""
#
#     while not is_valid_input:  # While not false, continue loop
#
#         try:
#             guess = int(input("Guess: "))
#             is_valid_input = True
#
#         except ValueError:
#             print("Invalid integer")
#             guess = int(input("? "))
#     return guess
#
#
# def load_number(filename):
#
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid contents in {filename}")
#         number = 6  # when file is have invalid data, 6 will be the new guessing number
#     except FileExistsError:
#         print(f"{filename} not found")
#         number = 4
#     else:
#         infile.close()
#
#     return number
#
#
# main()


# name = ["tom","john","jason"]
# age = ["15","20","23"]
#
# user_info=[]
# for x in range(len(name)):
#     user_info.append(name[x],age[x])



try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")