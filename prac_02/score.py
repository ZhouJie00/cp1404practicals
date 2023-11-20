import random
def grade_score(score):
    if score < 0 or score > 100:
        score = "Invalid score"
    elif score > 90:
        score="Excellent"
    elif score > 50:
        score="Passable"
    else:
        score="Bad"
    return score


# stop score_menu.py from executing main() from score.py, commenting this is needed

# def main():
#     score = random.randint(0,120)
#     print(f"your score is {score}, grade: {grade_score(score)}")
#
# main()

