# ------------------------------------------------> class

# class student:
#     # def asigndata(self,roll,name):
#     #     self.roll=roll
#     #     self.name=name
#     def __init__(self,roll,name): #--------------->constructor
#         self.roll=roll
#         self.name=name

#     def display(self):
#         print("roll no is",self.roll)
#         print("name is",self.name)
    
# s1=student(1,"sanika")
# # s1.asigndata(1,"sanika")
# s1.display()



# class student:
#     clg="walchand clg"             #-----------------------> static variable/class member variable
#     def __init__(self,roll,name):
#         self.roll=roll
#         self.name=name

#     def display(self):
#         print("roll no is",self.roll)
#         print("name is",self.name)
#         print("clg is",self.clg)
#         # print(student.clg)

# s1=student(1,"sanika")
# s1.clg="abcd"
# s1.display()
# s2=student(2,"patil")
# print(s1.clg)
# print(s2.clg)
# student.clg="pqrst"
# print(s1.clg)
# print(s2.clg)


# #----------------------------------------> static method

# class student:
#    a=10
#    @staticmethod 
#    def msg():
#       print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

# # s1=student()
# # s1.msg()
# print(student.a)
# (student.msg())


# #----------------------------------------> inheritance

# class parent:
#     a=10     #static variable 

# class child(parent):
#     def fun(self):
#         print(self.a)

# c1=child()
# print(c1.a)
# c1.fun()

# class parent:
#     def _home(self):                 #protected
#         print("parent home method")

# class child(parent):
#     pass

# c=child()
# c._home()                            #protected



# #----------------------------------------->multilvel
# class parent:
#     def home(self):
#         print("parents home")
# class child(parent):
#     def home(self):
#         print("child home")
# class granchild(child):
#     pass
# c=granchild()
# c.home()

# #----------------------------------------->multiple
# class parent:
#     def home(self):
#         print("parents home")
# class parent2():
#     def home(self):
#         print("child home")
# class granchild(parent,parent2):
#     pass
# c=granchild()
# c.home()

# #----------------------------------------->hirarchical
# class parent:
#     def home(self):
#         print("parents home")

# class child(parent):
#     def home(self):
#         print("child home")
# class child1(parent):
#     pass
# c=granchild()
# c.home()


##-------------------------------------------> super().__init__(age,name)
# class person:
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name
    
# class student(person):
    
#     def __init__(self,age,name,marks,total):
#         super().__init__(age, name)
#         self.marks=marks
#         self.total=total

#     def display(self):
#         print("name",self.name)
#         print("age",self.age)
#         print("marks",self.marks)
#         print("total",self.total)

# class teacher(person):
#     def __init__(self,age,name,salary):
#         super().__init__(age, name)
#         self.salary=salary

#     def display(self):
#         print("name",self.name)
#         print("age",self.age)
#         print("salary",self.salary)


# t=teacher(15,"sanika",25000)
# t.display()

# s=student(12,"s",78,100)
# s.display()


# class Student:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
    
#     def display(self):
#         print("Age:", self.age)
#         print("Name:", self.name)


# class Sports(Student):
#     def __init__(self, age, name, extra_marks):
#         super().__init__(age, name)
#         self.extra_marks = extra_marks
    
#     def display(self):
#         super().display()
#         print("Extra Marks (Sports):", self.extra_marks)


# class Academic(Student):
#     def __init__(self, age, name, m1, m2, m3):
#         super().__init__(age, name)
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def calculate_total(self):
#         return self.m1 + self.m2 + self.m3
    
#     def display(self):
#         super().display()
#         print("Marks:", self.m1, self.m2, self.m3)
#         print("Total Academic Marks:", self.calculate_total())


# s1 = Sports(18, "Rohan", 10)
# s2 = Academic(18, "Rohan", 70, 80, 90)

# s1.display()
# print()
# s2.display()
    