 
for i in range(1, 21, 2):
    if (i%2) != 0:
        print(i, end=' ')
print()



# a. count in 10s from 0 to 100
for i in range(101):
    if i==10 or i==20 or  i==30 or  i==40 or  i==50 or  i==60 or  i==70 or  i==80 or  i==90 or i == 100 :
        print(i, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20,0,-1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
inputStars = int(input("Number of stars: "))
stars = ""
for i in range(inputStars):
    stars += "*"
    print(stars)



# d. print n lines of increasing stars. Using the same number
# as above, print lines of increasing stars, starting at 1 with no blank line.
# E.g., if the user entered 4, your single loop should print:



test_value = 23.5555555
print(f"this number should be in 3 decimal place Ans: {test_value:.2f}")
print("this number should be in 3 decimal place Ans: {0:.2f}".format(test_value))