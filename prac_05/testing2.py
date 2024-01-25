d1={}

d1["Item1"]="I1"
print(d1)
month={1:"Jan",2:"Feb",3:"Mar",4:"Apr"}
print(month)

for x in month:
    print("Key: ",x," Value:",month[x])

del(month[2])
print(month)


print("----------------")

student_dict={'101':"Marry Tan","102":"Peter Pan","103":"Joe Lim"}

print(student_dict["102"])#Peter Pan
print(student_dict.get("1022"))
print(student_dict.get("103","not found")) #Joe Li
print(student_dict.get("104","not found")) #Not found

s= student_dict.get("Mary Tan","Not Found")#Not Found
print(s)

print("----------------")
student_dict["105"]="Nill"

for x in student_dict:
    print(x,student_dict[x])


if "Marry Tan" not in student_dict:
    print("Not Found") #not found
else:
    print("found")


if "101"  in student_dict:
    print("Found") #found
else:
    print("Not found")

if "Marry Tan" in student_dict.values():
    print("Found") #found
else:
    print("Not found")

if "Peter" in student_dict.values():
    print("Found") #found
else:
    print("Not found")
print("----------------------")


student_dict.clear()
print(student_dict) #{}
print("EEEEEE")

dictionary = {'101': "Mary Tan", '102': "Peter Pan", '103': "Joe Lim"}

size = len(dictionary)
list1 = list(dictionary.keys())
list2 = list(dictionary.values())
list3 = list(dictionary.items())

print(size)
print(list1)
print(list2)
print(list3)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print("-----------------                 -----directory_list")


cDirect={"Jane":[4,2,1],"Tom":[6,3,1],"Jake":[6,2,1]}

# for x in cDirect:
#     for n in cDirect[x]:
#         print(n)

for x in cDirect:
    print(cDirect[x][0],cDirect[x][1],cDirect[x][2])
# 4 2 1
# 6 3 1
# 6 2 1
print("--------------------------")
cDirect["Onee"]=[6,5,2]


for x in cDirect:
    print(cDirect[x][0],cDirect[x][1],cDirect[x][2])
# 4 2 1
# 6 3 1
# 6 2 1
# 6 5 2


print("--------------------------DirectoryInsideDirectory")

a={"a123":{"Name":"Jo","num":1231},"b123":{"Name":"zh","num":9142}}


for x in a:
    print(x) #a123,b123

    print(a[x]["Name"],a[x]["num"])







x, y = (1, 2)  # (1, 2) is a tuple
print(x, type(x))  # 1 <class 'int'>
print(y, type(y))

def hh():
    return 5,9

print(hh())