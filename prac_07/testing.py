# class Student:
#     def __init__(self, first_name="", last_name="", student_id=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = student_id
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.id})"
#
#     # Simple example class usage (client code)
#
#
#
#
# first_name = input("First name: ")
# last_name = input("Last name: ")
# student_id = int(input("ID: "))
# s1 = Student(first_name, last_name, student_id)
# print(s1.first_name, "has ID", s1.id)
# print(s1)
#

class Plant:

    def __init__(self, name="", height=0.0, growth_rate=1.0):
        self.name = name
        self.height=height
        self.growth_rate=growth_rate

    def feed(self,water):
        self.height+= water*self.growth_rate

    def __str__(self):
        return f'{self.name} {self.height} {self.growth_rate}'

p1 = Plant("flower",1,1.5)

print(p1)
p1.feed(20)
print(p1)