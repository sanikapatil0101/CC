#-----------------------------------------------> function overloading


# class ex:
#     def add(self,a,b):
#         print("addition of two nos",a+b)
        
#     def add(self,a,b,c):
#         print("addition of 3 nos",a+b+c)

# e1=ex()
# # e1.add(1,2,3)
# e1.add(1,2)



# class ex:
#     def add(self , a, b, c=None):
#         if c==None:
#             print("2 number addition ",a+b)
#         else:
#             print("3 number addition ",a+b+c)

# e1=ex()
# e1.add(1,2,3)
# e1.add(1,2)


# class ex:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         print(x+y)

#     def __add__ (self,other):
#         return ex(self.x + other.x , self.y + other.y)
    
#     def __gt__(self,other):
#         return self.x>other.x
    
#     def __str__(self):
#         return (f"{self.x},{self.y}")

# e1=ex(11,12)
# e2=ex(1,2)
# print(e1+e2)


# class Student:
#     def __init__(self):
#         self.roll = 0
#         self.name = ""
#         self.m1 = 0
#         self.m2 = 0
#         self.m3 = 0
#         self.total = 0
#         self.per = 0.0

#     def accept(self):
#         self.roll = int(input("Enter Roll Number: "))
#         self.name = input("Enter Name: ")
#         self.m1 = int(input("Enter Marks of M1: "))
#         self.m2 = int(input("Enter Marks of M2: "))
#         self.m3 = int(input("Enter Marks of M3: "))

#     def calculate(self):
#         self.total = self.m1 + self.m2 + self.m3
#         self.per = self.total / 3

#     def __str__(self):
#         return (f"Roll Number: {self.roll}\n"
#                 f"Name: {self.name}\n"
#                 f"Marks: {self.m1}, {self.m2}, {self.m3}\n"
#                 f"Total: {self.total}\n"
#                 f"Percentage: {round(self.per, 2)}")

# s = Student()
# s.accept()
# s.calculate()
# print(s)     


# class Example:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def accept(self):
#         self.x = int(input("Enter x: "))
#         self.y = int(input("Enter y: "))

#     def calculate(self, e1,e2):
#         e2.x = e1.x + e2.x
#         e2.y = e1.y + e2.y

#     def display(self):
#         print("x =", self.x, " y =", self.y)


# print("Enter data for e1:")
# e1 = Example()
# e1.accept()

# print("Enter data for e2:")
# e2 = Example()
# e2.accept()

# e2.calculate(e1,e2)

# print("After Calculation")
# print("Object e1:")
# e1.display()

# print("Object e2:")
# e2.display()


# class parent:
#     def car(self):
#         print("from parent car")
    
# class child(parent):
#     def car(self):
#         print("BMW")

# c=child()
# c.car()


# #duck and quack 
# class cat:
#     def sound(self):
#         print("meoww...")
# class dog:
#     def sound(self):
#         print("bark..")
        
# def makesound(animal):
#     animal.sound()
    
# makesound(cat())
# makesound(dog())



# #### encapsulation
# class BankAccount:
#     def _init_(self,owner,bal):
#         self.owner=owner        ##public
#         self.__bal=bal          ##private
#     def deposit(self,am):
#         if am>0:
#             self.__bal+=am
#         print(f"{am} deposited")
#         print(f"{self.__bal} new balance")
        
#     def withdraw(self,amt):
#         if 0<amt<=self.__bal:
#             self.__bal-=amt
#             print(f"{amt} withdrwa")
#             print(f"{self.__bal} new balance")
#         else:
#             print("balance insufficient")
#     def getbal(self):
#         print(f"the balance is {self.__bal}")

# acc=BankAccount("Jyoti",10000)

# print("owner name ",acc.owner)
# # print("balance",acc.bal)### give error
# acc.deposit(500)
# acc.withdraw(200)
# acc.getbal()


# class bankaccount():
#     def __init__(self,owner,bal):
#         self.owner=owner            #public
#         self.__bal=bal              #private
    
#     def deposit(self,amt):
#         if amt>0:
#             self.__bal+=amt
#         print(f"{amt} deposited")
#         print(f"{self.__bal} new bal")
        
#     def withdraw(self,amt):
#         if 0 < amt <= self.__bal:
#             self.__bal-=amt
#         print(f"{amt} withdrawl..")
#         print(f"{self.__bal} new bal")
        
#     def getbal(self):
#         print(self.__bal)
        
        
# acc=bankaccount("raj",10000)
# print("owner name",acc.owner)
# #print("balance",acc.__bal)
# acc.deposit(500)


# from abc import ABC,abstractmethod

# class boss(ABC):
#     @abstractmethod
#     def task1(self):
#         pass
        
#     def salary(self):
#         print("salary 100000")
        
# class emp(boss):
#     def task1(self):
#         print("task completed")
        
# e=emp()
# e.salary()



# from abc import ABC,abstractmethod

# class boss(ABC):
#     @abstractmethod
#     def task1(self):
#         pass
        
#     def salary(self):
#         print("salary 100000")
        
# class emp1(boss):
#     def task1(self):
#         print("task completed")
        
# class emp2(boss):
#     def task1(self):
#         print("task completed")
        
# e=emp1()
# e.salary()
# e=emp2()
# e.salary()





#-----------------------------------------------------> linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

class linkedlist:
    def displayList(self,s):            #------------------------------>display
        if s==None:
            print("empty list")
        else:
            while s!=None:
                print(s.data,end="->")
                s=s.next
            print("None")

    def createNode(self):
        self.data=int(input())
        return node(self.data)
    
    def insertNodeatFirst(self,s):      #---------------------->insert at first
        temp=self.createNode()
        if s==None:
            s=temp
        else:
            temp.next=s
            s=temp
        return s

    def insertNodeatLast(self,s):      #---------------------->insert at last
        temp=self.createNode()
        if s==None:
            s=temp
        else:
            s1=s
            while s1.next!=None:
                s1=s1.next
            s1.next=temp
        return s
    
    def insertNodeatIndex(self,s,i):    #---------------------> insert at index i

        lenn=0
        t=s
        while t is not None:
            lenn+=1
            t=t.next
        if i==0:
            return self.insertNodeatFirst(s)
        elif i>lenn:
            print("invalid index")
            return s
        elif i==lenn:
            return self.insertNodeatLast(s)
        else:
            temp=self.createNode()
            k=0
            s1=s
            while k<i-1:
                s1=s1.next
                k+=1
            temp.next=s1.next
            s1.next=temp
            return s
        
    def deleteatFirst(self,s):      #-------------------->delete first
        s1=s
        if s==None:
            print("empty list so cannot delete")
            return s
        return s.next
    
    def deleteatLast(self,s):       #-------------------->delete last
        if s==None:
            print("empty list so cannot delete")
        if s.next==None:
            print("only one node present cannot delete")
        else:
            s1=s
            while s1.next.next is not None:
              s1=s1.next
            s1.next=None
        return s
    
    def deleteatIndex(self,s,i):   #-------------------->delete at index
        lenn=0
        t=s
        while t is not None:
            lenn+=1
            t=t.next
        if i==0:
            return self.deleteatFirst(s)
        elif i>lenn:
            print("invalid index")
            return s
        elif i==lenn-1:
            return self.deleteatLast(s)
        else:
            k=0
            s1=s
            while k<i-1:
                s1=s1.next
                k+=1
            s1.next=s1.next.next
            return s
        
    def findValue(self,s,v):    #-------------------->find index of value
        if s==None:
            print("empty list")
            return -1
        ind=0
        s1=s
        while s1!=None:
            if s1.data==v:
                return ind
            s1=s1.next
            ind+=1
        print("value not found")
        return -1
    
    def findValuebyIndex(self,s,i):    #-------------------->find value by index
        if s==None:
            print("empty list")
            return -1
        ind=0
        s1=s
        while s1 is not None and ind<i:
            s1=s1.next
            ind+=1
        if s1 is None:
            print("invalid index")
            return -1
        return s1.data

        
    def deleteByValue(self,s,v):     #-------------------->delete by value
        i=self.findValue(s,v)
        if i==-1:
            print("value not present, so cannot delete")
            return s
        s=self.deleteatIndex(s,i)
        return s
    
    def count(self,s):              #--------------------->count node
        s1=s
        c=0
        while s1 is not None:
            s1=s1.next
            c+=1
        return c
    
    def evenNo(self,s):              #--------------------->even number
        if s==None:
            print("empty list")
            return -1
        s1=s
        li=[]
        while s1!=None:
            if s1.data%2==0:
                li.append(s1.data)
            s1=s1.next
        print("even numbers from list are")
        return li

    def oddNo(self,s):                 #--------------------->odd number
        if s==None:
            print("empty list")
            return -1
        s1=s
        li=[]
        while s1!=None:
            if s1.data%2==1:
                li.append(s1.data)
            s1=s1.next
        print("odd numbers from list are")
        return li
    
    def isprimenode(self,s):            #---------------------> prime number
        if s==None:
            print("empty list")
            return -1
        s1=s
        li=[]
        while s1!=None:
            if isprime(s1.data):
                li.append(s1.data)
            s1=s1.next
        print("priem numbers from list are:")
        return li
    
    def middleNode(self, s):              #---------------------->returns middle node
        slow = s
        fast = s
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("middle node data is: ")
        return slow.data
    
    def reverseLink(start,s):             #----------------------> revrse link
        prev=None
        curr=s
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        print("reversed list")
        return prev
    
    def isPalindrome(self, s):          #---------------------->checks palindrome
        if s is None or s.next is None:
            return True
        slow = s
        fast = s
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = self.reverseLink(slow.next)
        first = s
        temp = second
        while temp is not None:
            if temp.data != first.data:
                return False
            temp = temp.next
            first = first.next
        print("list is palindrome:")

        return True
    
    def duplicates(self,s):       #---------------->print duplicates
        l1=[]
        l2=[]
        s1=s
        while s1 is not None:
            if s1.data not in l1:
                l1.append(s1.data)
            else:
                l2.append(s1.data)
            s1=s1.next
        print("duplicates elements from list")
        return l2
    

    def removeDupliSorted (self,s):    #-------------->removed duplicates from sorted list
        if s is None:
            return s
        s1=s
        while s1 is not None and s1.next is not None:
            if s1.data==s1.next.data:
                s1.next=s1.next.next
            else:
                s1=s1.next
        print("removed duplicates from sorted list")
        return s
    

    def removeDupliUnsorted(self,s):       #---------------->print duplicates from unsorted list
        if s is None:
            return s
        seen = set()        
        curr = s
        seen.add(curr.data) 
        while curr is not None and curr.next is not None:
            if curr.next.data in seen:            
                curr.next = curr.next.next        
            else:
                seen.add(curr.next.data)          
                curr = curr.next                  
        print("Removed duplicates from unsorted list")
        return s







    




# start=node(10)
# start.next=node(20)
# start.next.next=node(30)
# print(start.data,end="->")
# print(start.next.data,end="->")
# print(start.next.next.data,end="->")
# print(start.next.next.next)


start=None
l=linkedlist()
# start=l.insertNodeatFirst(start)
# start=l.insertNodeatFirst(start)
# start=l.insertNodeatFirst(start)
# l.displayList(start)
start=l.insertNodeatLast(start)
start=l.insertNodeatLast(start)
start=l.insertNodeatLast(start)
start=l.insertNodeatIndex(start,2)
start=l.insertNodeatFirst(start)
start=l.insertNodeatFirst(start)
start=l.insertNodeatIndex(start,3)
# start=l.deleteatFirst(start)
# start=l.deleteatLast(start)
# start=l.deleteatIndex(start,2)
# start=l.deleteByValue(start,12)
# print(l.count(start))
# print(l.evenNo(start))
# print(l.oddNo(start))
# print(l.isprimenode(start))
# print(l.middleNode(start))
# print(l.isPalindrome(start))
# print(l.duplicates(start))
# start=l.removeDupliSorted(start)
start=l.removeDupliUnsorted(start)
l.displayList(start)

