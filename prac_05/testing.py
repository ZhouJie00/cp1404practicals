d1={}

a=5
# print((help(a)))

month={1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr"}
del(month[2]) #mar
print(month) #{1: 'Jan', 3: 'Mar', 4: 'Apr'}
            # Index don't change , not like list
print(month[3])

print("----------------")

stud_dict = {'101': "Mary Tan", '102': "Peter Pan", '103': "Joe Lim"}

print(stud_dict["102"])#Peter Pan

s= stud_dict.get("103")
s= stud_dict.get("103","Not Found")#Joe Lim #ONLY FIND VALUE FROM KEY
print(s)

s= stud_dict.get("104","Not Found")#Not Found
print(s)

s= stud_dict.get("Mary Tan","Not Found")#Not Found
print(s)

stud_dict["105"]="Nill"

print(stud_dict) #{'101': 'Mary Tan', '102': 'Peter Pan', '103': 'Joe Lim', 105: 'Nill'}

if "Mary Tan" not in stud_dict:
    print("\n"+"Not found"+"\n") #not found
else:
    print("\n"+"exist"+"\n")
print("-----------------")


if "102" not in stud_dict:  #only check key
    print("\n"+"Not found"+"\n") #exist
else:
    print("\n"+"exist"+"\n")
print("-----------------")


print(stud_dict["102"])
print("-----------------")
for x in stud_dict:
    print(x) #key
    print(stud_dict[x]) # 101           Value
                        # Mary Tan
                        # 102
                        # Peter Pan
                        # 103
                        # Joe Lim
                        # 105
                        # Nill

print("-----------------")
for key, value in stud_dict.items():
    print(key, value)#101 Mary Tan
                     # 102 Peter Pan
                     # 103 Joe Lim
                     # 105 Nill

print("-----------------")

print(len(stud_dict))#4
print(list(stud_dict.keys())) #['101', '102', '103', '105']
print(list(stud_dict.items())) #[('101', 'Mary Tan'), ('102', 'Peter Pan'), ('103', 'Joe Lim'), ('105', 'Nill')]

stud_dict.clear() #{}
print(stud_dict)

print("-----------------&")
dictionary = {'101': "Mary Tan", '102': "Peter Pan", '103': "Joe Lim"}

l={}
# l=dictionary
# for x in l:
#
#     print(l)

for x in dictionary:   #same as i=dictionary
    l[x]=dictionary[x] # l list key = dic value
    print(l)
print(l) #{'101': 'Mary Tan', '102': 'Peter Pan', '103': 'Joe Lim'}


size = len(dictionary)
list1 = list(dictionary.keys())
list2 = list(dictionary.values())
list3 = list(dictionary.items())
print(size) # 3
print(list1) # ['101', '102', '103']
print(list2) # ['Mary Tan', 'Peter Pan', 'Joe Lim']
print(list3) # [('101', 'Mary Tan'), ('102', 'Peter Pan'), ('103', 'Joe Lim')]




print("------------------------------------------------------------------")
#------------------------------------------------------------------

test_dir1={"a123":"jim","a231":"tom","d312":"Je"}

print(test_dir1["a231"]+"\n")
for i in test_dir1:
    print(i)
    print(test_dir1[i])


if "jim" not in test_dir1: #not exist
    print("not exist")
else:
    print("exist")

                        #test_dir1=test_dir1.key()  if .... by default
if "jim" not in test_dir1.keys(): #not exist
    print("not exist")
else:
    print("exist")

if "a231" not in test_dir1.keys(): #exist
    print("not exist")
else:
    print("exist")

print("------------------------------------")
#------------------------------------
#test_dir1={"a123":"jim","a231":"tom","d312":"Je"}



if "jim" not in test_dir1.values(): #exist
    print("not exist")
else:
    print("exist")

if "a123" not in test_dir1.values(): #not exist
    print("not exist")
else:
    print("exist")
#------------------------------------
#test_dir1={"a123":"jim","a231":"tom","d312":"Je"}

if "jim" not in test_dir1.keys() and "jim" not in test_dir1.values(): #exist
    print("not exist")
else:
    print("exist")
