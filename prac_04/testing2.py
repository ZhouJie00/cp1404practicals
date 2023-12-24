s1="Thisisastring"

print(s1[0])
print(s1[1])
print(s1[2])

print("-----------------1")
print(s1[-1])
print(s1[-2])
print(s1[-3])
print("-----------------2")
print(s1[0:2])
print(s1[0:5])
print(s1[3:5])
print("-----------------3")
print(s1[0:])
print(s1[2:])
print(s1[:2])
print(s1[:2])
print("-----------------4")
print(s1[:-1])
print(s1[::-1])
print("-----------------5")
print(s1[0:6:2])
print(s1[0:-1:2])
print(s1[-5:-1])   #always from left!
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