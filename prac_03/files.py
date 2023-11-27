


#block 1
name = input("Please enter your name: ")
out_file = open("name.txt","w")
out_file.write(name+"\n")
out_file.close()

#block 2
in_file = open("name.txt")
for name in in_file:
    print(f"Your name is {name}")



#block 3
in_file = open("numbers.txt")
number_list = in_file.readlines()
sum_numbers = 0
for i in range(2): # index 0 and 1
    sum_numbers += int(number_list[i].strip("\n"))
print(sum_numbers)

in_file.close()


#block 4
in_file = open("numbers.txt")

for numbers in in_file:
    print(numbers)

in_file.close()