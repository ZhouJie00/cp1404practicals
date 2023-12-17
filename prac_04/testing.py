from operator import itemgetter

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

things.append(21)
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

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
data.sort()
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

print("------------------------------")

words= 'this is a test'.split()
#Gives ['this','is','a','test']
print(words)

words= 'this is a test'.split()
for i in range(len(words)):
    words[i] = words[i].title() # capital the first char
text = ','.join(words)
#['This', 'Is', 'A', 'Test']
print(text)

print("------------------------------")

stuff = (4,5,6)
print(type(stuff)) #<class 'tuple'>
print(stuff.index(5)) #1， index of 5 is at 1
# print(stuff.index(10)) #will not show anything when no found

def format_date (day, month, year):
    return f"{day}/{month}/{year}"
date = (22, 11, 1988) # this is a tuple

a= format_date(*date)
print(a)
#* unpacks date tuple

