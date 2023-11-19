MINI_PASS_LENGTH = 10


def main():
    password = get_password()
    while len(password) < MINI_PASS_LENGTH:
        print("Please enter a password with a minimum length of 10 characters")
        password = get_password()

    asterisk_password = get_asterisk(password)
    print(asterisk_password)


def get_password():  # get password
    password = input("please enter a password: ")

    return password


def get_asterisk(password):  # get asterisk
    asterisk_password = ""
    for i in range(len(password)):
        asterisk_password += "*"

    return asterisk_password


main
