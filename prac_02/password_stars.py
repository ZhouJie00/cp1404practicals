

MINI_PASS_LENGTH = 10



def main():
    password = input("please enter a password: ")
    while len(password) < MINI_PASS_LENGTH:
        print("Please enter a password with a minimum length of 10 characters")
        password = input("please enter a password: ")

    asterisk_password = ""
    for i in range(len(password)):
        asterisk_password += "*"

    print(asterisk_password)

main()

