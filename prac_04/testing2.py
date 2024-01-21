s1="Thisisastring"

print(s1[0])  #"T"
print(s1[1])  #"h"
print(s1[2])  #"i"

print("-----------------1")
print(s1[-1])  #"g"
print(s1[-2])  #"n"
print(s1[-3])  #"i"

s1="Thisisastring"
print("-----------------2")
print(s1[0:2])  #"Th"
print(s1[0:5])  #"Thisi"
print(s1[3:5])  #"si"

s1="Thisisastring"
print("-----------------3")
print(s1[0:])  #"Thisisastring"
print(s1[2:])  #"isisastring"
print(s1[:2])  #"Th

s1="Thisisastring"
print("-----------------4")
print(s1[:-1])  #"Thisisastrin"
print(s1[::-1])  #"gnirtsasisihT"

s1="Thisisastring"
print("-----------------5")
print(s1[0:6:2])   #"Tii"
print(s1[0:-1:2])  #"Tiiati"
print(s1[-5:-1])   #trin
                   #always from left!
                   #print(s1[-1:-5]) Does not work!


print(s1[::])#Thisisastring
print(s1[::-1])#gnirtsasisihT
print("-----------------6")

choice = "dWAdadc".lower()
print(choice)#dwadadc

choice = "dWAdadc".upper()
print(choice)#DWADADC

choice = "dWAdadc".title()
print(choice)#Dwadadc #cap first, and decap rest

choice = "dWAdadc".swapcase()
print(choice)#DwaDADC

choice = "dWAdadc".count("d")
print(choice)#3

choice = "dWAdadc".find("c")
print(choice)#6, index 6

subject_code = "CP123"
if "CP" in subject_code:
    print("value is not found")

if "CA" not in "CP123":
    print("value is not found")

message = '     Learn Python  '
print('Message:',message.replace("a", ""))#     Lern Python



# remove leading and trailing whitespaces

print('Message:', message.strip())#Learn Python
print('Message:', message.rstrip())#     Learn Python



d1 = "apple,banana,cherry,dates"
items = d1.split(",")  # Split the string by comma
print(items)  # Output: ['apple', 'banana', 'cherry', 'dates']

data = "Alice-John-Eve-Bob"
names = data.split("-")  # Split the string by hyphen
print(names)  # Output: ['Alice', 'John', 'Eve', 'Bob']

string = "?name=Bob&age=99&day=Wed"



string = string[1:] #remove ?
print(string)
string_list = string.split("&") #['name=Bob', 'age=99', 'day=Wed']
print(string_list)

string_list_2 = []
temp_list = []
for i in range(len(string_list)):
    temp_list = string_list[i].split("=")
    string_list_2.append((temp_list[0],temp_list[1]))


print(string_list_2)


# The enumerate function in Python is a built-in function used to add a counter
# to an iterable (like a list, tuple, or string), and it returns it as an enumerate object.
# just to indicate index that's all
# X = index Y= value
values = (2, 4, 6)
for x, y in enumerate(values):
     print("{0}:{1:.0f}".format(x, y), end=" ")
# 0:2 1:4 2:6

print("")
values = ['a', 'b', 'c']
for index, value in enumerate(values, 1):  # Starts index counting from 1
    print(index, value)
# 1 a
# 2 b
# 3 c

print(sum([1, 2, 1, 2, 1]))
#The sum of the set is 7
sum({1, 2, 1, 2, 1})
"The sum of the set {1, 2, 1, 2, 1} is 3. This is because (sets) only hold unique elements"