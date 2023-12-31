import score as scoring


# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit


def check_score(score):
    while score < 0 or score > 100:
        print("please enter a valid score!")
        score = int(input("Please enter a score: "))
    return score


def get_stars(score):
    stars = ""
    for i in range(score):
        stars += "*"

    return  stars

def main():
    menu = " (G)et a valid score (must be 0-100 inclusive)\n (P)rint result (copy or import your function to determine the result from score.py)\n (S)how stars (this should print as many stars as the score)\n (Q)uit"
    print(menu)
    score = ""
    option = input("Enter an option: ").upper() # Qus: In main(), before the menu loop, get a valid score using your function.

    while option != "Q": #menu
        if option == "G":
            score = int(input("Please enter a score: "))
            score = check_score(score)

        elif option == "P":
            print(f"your score: {score}, grade: {scoring.grade_score(score)}")

        elif option == "S":
            print(f"stars: {get_stars(score)}")
        else:
            print("Please enter a valid input!")

        print(menu)
        option = input("Enter an option: ").upper()


    print("Farewell")

main()
