# # ----------------------------------> doubly linked list

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None

# class doublyLink:
#     def displyaList(self,s): 
#         s=start
#         if s is None:
#             print("empty list")
#         else:
#          while s is not None:
#              print(s.data,end="->")
#              s=s.next
#         print("None")
    

#     def reverseList(self,s):
#         s1=s
#         if s1==None:
#             print("empty list")
#         while s1.next is not None:
#             s1=s1.next
#         while s1 is not None:
#             print(s1.data,end="->")
#             s1=s1.prev
#         print("None")


#     def createNode(self):
#         data=int(input("enter data for node:"))
#         return node(data)
    
#     def count(self,s):              #--------------------->count node
#         s1=s
#         c=0
#         while s1 is not None:
#             s1=s1.next
#             c+=1
#         return c
    
#     def insertatFirst(self,s):
#         temp=self.createNode()
#         if s==None:
#             s=temp
#         else:
#             temp.next=s
#             s.prev=s
#             s=temp 
#         return s
    

#     def inserAtlast(self,s):
#         s1=s
#         temp=self.createNode()
#         if s1==None:
#             s=temp
#         else:
#             while s1.next is not None:
#                 s1=s1.next
#             temp.prev=s1
#             s1.next=temp
#         return s
    
#     def insertAtInd(self,s,i):
#         s1=s
#         lenn=self.count(s)
#         if i==0:
#             return (self.insertatFirst(s))
#         elif i==lenn:
#             return (self.inserAtlast(s))
#         elif i>lenn:
#             return ("Inavlid index")
#         else:
#             temp=self.createNode()
#             k=0
#             while k<i-1:
#                 s1=s1.next
#                 k+=1
#             temp.next=s1.next
#             temp.prev=s1
#             if s1.next is not None:
#                 s1.next.prev=temp
#             s1.next=temp
#             return s
        
#     def finbyValue(self,s,v):
#         s1=s
#         while s1 is not None:
#             if s1.data==v:
#                 return True
#             s1=s1.next
#         return False
    
#     def deleteFirst(self,s):
#         # s1=s
#         if s==None:
#             print("cannot delete")
#             return s
#         if s.next is None:
#             return None
#         print("Deleted:", s.data)
#         s=s.next
#         s.prev=None
#         return s
    
#     def deleteLast(self,s):
#         if s==None:
#             print("cannot delete")
#             return s
#         if s.next is None:
#             return None
#         s1=s
#         while s1.next is not None:
#             s1=s1.next
#         s1.next.prev=None
#         s1.next=None    
#         return s

#     def findValue(self,s,v):    #-------------------->find index of value
#         if s==None:
#             print("empty list")
#             return -1
#         ind=0
#         s1=s
#         while s1!=None:
#             if s1.data==v:
#                 return ind
#             s1=s1.next
#             ind+=1
#         print("value not found")
#         return -1

#     def deleteByValue(self,s,v):     #-------------------->delete by value
#         i=self.findValue(s,v)
#         if i==-1:
#             print("value not present, so cannot delete")
#             return s
#         s=self.deleteatIndex(s,i)
#         return s
    

# # start=None
# # start=node(10)
# # start.next=node(20)
# # start.next.prev=start
# # start.next.next=node(30)
# # start.next.next.prev=start.next
       

# d=doublyLink()  
# # print(start.data,end="->")  
# # print(start.next.data,end="->")  
# # print(start.next.next.data,end="->")  
# # print("None")
# start=None
# start=d.insertatFirst(start)
# start=d.insertatFirst(start)
# start=d.insertatFirst(start)
# start=d.deletFirst(start)
# # start=d.inserAtlast(start)
# # start=d.inserAtlast(start)
# # start=d.insertAtInd(start,3)
# # print(d.reverseList(start))
# print(d.displyaList(start))
# print(d.finbyValue(start,7))






# #---------------------------------------> circular linked list
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=next

# class circularll:
#     def displaylist(self,s):
#         if s==None:
#             print("empty list")
#         s1=s
#         while True:
#             print(s1.data,end="->")
#             s1=s1.next
#             if(s1==s):
#                 break

#     def createNode(self):
#         self.data=int(input("enter data: "))
#         return node(self.data)
    
#     def insertNodeatFirst(self,s):      #---------------------->insert at first
#         temp=self.createNode()
#         if s==None:
#             temp.next=temp
#             return temp
#         s1=s
#         while s1.next!=s:
#             s1=s1.next

#         temp.next=s
#         s1.next=temp
#         s=temp
#         return s

#     def insertNodeatLast(self,s):      #---------------------->insert at last
#         temp=self.createNode()
#         if s==None:
#             temp.next=temp
#             return temp
#         s1=s
#         while s1.next!=s:
#             s1=s1.next
#         s1.next=temp
#         temp.next=s
#         return s
    
#     def insertNodeatIndex(self,s,i):    #---------------------> insert at index i
#         lenn=0
#         t=s
#         while t.next!=s:
#             lenn+=1
#             t=t.next
#         if i==0:
#             return self.insertNodeatFirst(s)
#         elif i>lenn:
#             print("invalid index")
#             return s
#         elif i==lenn:
#             return self.insertNodeatLast(s)
#         else:
#             temp=self.createNode()
#             k=0
#             s1=s
#             while k<i-1:
#                 s1=s1.next
#                 k+=1
#             temp.next=s1.next
#             s1.next=temp
#             return s
        
#     def deleteatFirst(self,s):      #-------------------->delete first
#         s1=s
#         if s==None:
#             print("empty list so cannot delete")
#         while s1.next!=s:
#             s1=s1.next
#         s1.next=s.next
#         return s1.next
    
#     def deleteatLast(self,s):       #-------------------->delete last
#         if s==None:
#             print("empty list so cannot delete")
#         if s.next==None:
#             print("only one node present cannot delete")
#         else:
#             s1=s
#             while s1.next.next!=s:
#                 s1=s1.next
#             s1.next=s
#         return s
    
#     def deleteatIndex(self,s,i):   #-------------------->delete at index
#         lenn=0
#         t=s
#         while t.next!=s:
#             lenn+=1
#             t=t.next
#         if i==0:
#             return self.deleteatFirst(s)
#         elif i>lenn:
#             print("invalid index")
#             return s
#         elif i==lenn-1:
#             return self.deleteatLast(s)
#         else:
#             k=0
#             s1=s
#             while k<i-1:
#                 s1=s1.next
#                 k+=1
#             s1.next=s1.next.next
#             return s
        

#     def findValue(self,s,v):    #-------------------->find index of value
#         if s==None:
#             print("empty list")
#             return -1
#         ind=0
#         s1=s
#         while True:
#             if s1.data==v:
#                 print("value found at index: ",ind)
#                 return ind
#             s1=s1.next
#             ind+=1
#             if s1==s:
#               break
#         print("value not found")
#         return -1

#     def deleteByValue(self,s,v):     #-------------------->delete by value
#         i=self.findValue(s,v)
#         if i==-1:
#             print("value not present, so cannot delete")
#             return s
#         s=self.deleteatIndex(s,i)
#         return s

# start=None
# start=node(50)
# start.next=node(10)
# start.next.next=node(20)
# start.next.next.next=start
# c=circularll()
# # start.next.next.next.next=start
# start=c.insertNodeatFirst(start)
# start=c.insertNodeatLast(start)
# start=c.insertNodeatIndex(start,0)
# # start=c.deleteatIndex(start,1)
# # start=c.deleteByValue(start,12)
# # start=c.deleteatFirst(start)
# # start=c.deleteatLast(start)
# (c.displaylist(start))


#------------------------------------------------> stack using list and


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.stack=[]
        
    # def push(self,val):
    #     self.stack.append(val)
        
    # def isempty(self):
    #     return len(self.stack)==0
        
        
    # def pop(self):
    #     if self.isempty():
    #         return None
    #     return self.stack.pop()
    
    # def peek(self):
    #     if self.isempty():
    #         return None
    #     return self.stack[-1]
    
    # def printstack(self):
    #     print("stack is:",self.stack)

    def isempty(self):
        return self.top is None

    def push(self, val):
        temp = node(val)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isempty():
            print("Stack Underflow — cannot pop")
            return None
        
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.isempty():
            print("Stack is empty — no top element")
            return None
        return self.top.data

    def printstack(self):
        if self.isempty():
            print("Stack is empty")
            return
        temp = self.top
        print("Stack (TOP → BOTTOM): ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")    

from collections import deque

class Stack:
    def __init__(self):
        self.st = deque()

    def push(self, x):
        self.st.append(x)      

    def pop(self):
        if self.isEmpty():
            print("Stack empty")
            return None
        return self.st.pop()   

    def peek(self):
        if self.isEmpty():
            return None
        return self.st[-1]

    def isEmpty(self):
        return len(self.st) == 0

    def display(self):
        print(list(self.st))



s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.printstack()
print(s.pop())
s.printstack()
print(s.peek())
s.printstack()

    




#----------------------------------------------------->queue 

class QueueList:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)         

    def dequeue(self):
        if self.isEmpty():
            print("Queue empty")
            return None
        return self.q.pop(0)     

    def isEmpty(self):
        return len(self.q) == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.q[0]

    def display(self):
        print(self.q)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new = Node(x)
        if self.rear is None:           # first element
            self.front = self.rear = new
            return
        self.rear.next = new            # add at end
        self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue empty")
            return None
        val = self.front.data
        self.front = self.front.next    # remove from front
        if self.front is None:
            self.rear = None            # queue becomes empty
        return val

    def isEmpty(self):
        return self.front is None

    def peek(self):
        return None if self.front is None else self.front.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()





from collections import deque

class QueueDeque:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)    

    def dequeue(self):
        if not self.q:
            print("Queue empty")
            return None
        return self.q.popleft()  

    def peek(self):
        return None if not self.q else self.q[0]

    def isEmpty(self):
        return len(self.q) == 0

    def display(self):
        print(list(self.q))

