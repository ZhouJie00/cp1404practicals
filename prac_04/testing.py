from operator import itemgetter
from operator import attrgetter


#max(), min(), sum(), length(), sort <- for list
# sort cannot be used in tuple because the value inside it can't be changed


letters = list("Things") # new list ["T","h","i","n","g","s",]
print(letters)

things = [1,'a',True]
print(things)

subjects = ["CP1041","CP1404","CP2406"]
print(subjects[0])#CP1041
print(subjects[-1])#CP2406
print(subjects[-2])#CP1404

#things = ["one"] -> indexError:index out of range

names =["tommy","Juan","Vive"]

# user_name_option = int(input("Please enter name based on index: "))
# print(names[user_name_option])

scores = [40,89,67,51,61,95]
average = sum(scores)/len(scores)

print(average)
print(f"max: {max(scores)}")
print(f"min: {min(scores)}")
print(f"sum: {sum(scores)}")
print(f"length: {len(scores)}")
print(f"count data: {scores.count(67)}") #1, count how many 67 are there
scores.remove(89) #[40, 67, 51, 61, 95]
#scores.remove(1) <- will give ValueError, value not exist
print(scores)

del scores[3] #[40, 67, 51, 95], 4th element removed

print(scores)

scores.append(99) #[40, 67, 51, 95, 99]
print(scores)
scores.sort() #[40, 51, 67, 95, 99]
print(scores)
scores.reverse() #[99, 95, 67, 51, 40]
print(scores)

scores = [99, 95, 67, 51, 1, 40]

scores2 =scores.copy() #must put copy! If not won't create new!

scores2.reverse()
print(scores)
print(scores2)

print(sorted(scores)) #return a new list
print(list(reversed(scores))) #return a new list


scores.append(42) #[99, 95, 67, 51, 1, 40, 42]

print(scores)


things = [1,'a',True]

things.append(21)     #only way to create new index in list
things.append("EEEEE")

things[2] = "TRUE"

things[3] += 1
print(things) #[1, 'a', 'TRUE', 22, 'EEEEE']


subjects = ["CP1041","CP1404","CP2406"]
print("CP1041" in subjects) #True
print("CP1xxx" in subjects) #False

if "CP1041" in subjects:
    print("True")

[["Derek",7],["Carrie",8],["Bob",6],["Aaron",9]]


things= ['a',[1,2,3],'z']

print(things[1][0]) #1
things[1] #[1,2,3]
print([1,2,3][0]) #1
print("Python"[0]) #P


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
data = [7,8,6,9]
data.sort() #small to big
for record in data:
    print(record)
    # 6
    # 7
    # 8
    # 9

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
data = [[7], [8], [6], [9]]
data.sort() #small to big
for record in data:
    print(record)
    # [6]
    # [7]
    # [8]
    # [9]

    # itemgetter = for nested list or directory
    # small to big, default
    # A to Z,default
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort() #big to small
for record in data:
    print(record)
    # ['Aaron', 9]
    # ['Bob', 6]
    # ['Carrie', 8]
    # ['Derek', 7]

print("------------------------------")
data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(0))
for record in data:
    print(record)
    # ['Aaron', 9]
    # ['Bob', 6]
    # ['Carrie', 8]
    # ['Derek', 7]

print("------------------------------")

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1))
for record in data:
    print(record)
    # ['Bob', 6]
    # ['Derek', 7]
    # ['Carrie', 8]
    # ['Aaron', 9]

print("------------------------------")

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1),reverse=True) 
for record in data:
    print(record)
    # ['Aaron', 9]
    # ['Carrie', 8]
    # ['Derek', 7]
    # ['Bob', 6]

print("------------------------------")

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1,0)) # sort by second then first element
for record in data:
    print(record)
    # ['Aaron', 9]
    # ['Carrie', 8]
    # ['Derek', 7]
    # ['Bob', 6]

# attrgetter = for class sorting
# data = [Person(name="Bob", age=18), ...]
# data.sort(key=attrgetter("name"))


#for dictionary itemgetter
# data = [{'name': 'Derek', 'score': 7}, {'name': 'Carrie', 'score': 8}, {'name': 'Bob', 'score': 6}, {'name': 'Aaron', 'score': 9}]
# data.sort(key=itemgetter('score'))
print("------------------------------")

words= 'this is a test'.split()
#Gives ['this','is','a','test']
print(words)

words= 'this is a test'.split()
for i in range(len(words)):
        words[i] = words[i].title() # capital the first char
text = ','.join(words)
#This,Is,A,Test
print(text)

print("------------------------------")

stuff = (4,5,6)
print(type(stuff)) #<class 'tuple'>
print(stuff.index(5)) #1， index of 5 is at 1
# print(stuff.index(10)) #will not show anything when no found

def format_date (day, month, year):
    return f"{day}/{month}/{year}"

date = (22, 11, 1988) # this is a tuple
a = format_date(*date)
print(a)
#* unpacks date tuple


data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
numbers = [10, 0, -3, 50, -32, 64, 99, 200]
words = "CP1404 is a very good subject and I am HAPPY".split()


date_string = "12/5/2000" #Enter DOB (d/m/y)
parts = date_string.split("/") # this will be a list of strings
my_dob = (int(parts[0]), int(parts[1]), int(parts[2])) #put inside tuple, e.g. (12, 5, 2000)
print(my_dob)



myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)
print(x) #John#Peter#Vicky


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)
print(x)#nameTESTcountry



print(f"{2.522:.2f}")

s="He He"


print(list(s)) #return a new list
print(sorted(s))