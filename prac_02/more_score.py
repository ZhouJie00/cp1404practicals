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

def main():
    out_file = open("results.txt","a")
    processed_output = ""
    number_of_scores = int(input("numbers of scores you want to generate: "))
    list_score = ""
    for x in range(number_of_scores):
        score = random.randint(0,100)
        grade = grade_score(score)
        processed_output =f"{score} is {grade}\n"
        out_file.write(processed_output)
        print(processed_output)
    out_file.close()



main()