

name = "tom"

# try:
#     int(name)
#
# except ValueError as ex:
#     print(ex)
#


try:
    int(name)

except Exception as ex:
    print(ex)




def main():
    secret = load_number()
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it!")


def load_number(filename):
    infile= open(filename,"r")
    numer=