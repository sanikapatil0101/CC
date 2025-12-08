# class CQ:
#     def __init__(self,size):
#         self.size=size
#         self.que=[None]*size
#         self.front=-1
#         self.rare=-1
        
#     def enqueue(self,data):
#         if (self.rare+1)%self.size==self.front:
#             print("queue is full")
#             return
#         if self.front == -1:
#             self.front=0
#         self.rare=(self.rare+1)%self.size
#         self.que[self.rare]=data
#         print("inserted data",data)
        

#     def dequeue(self):
#         if self.front==-1:
#             print("queue is empty")
#             return
#         print("deleted element..",self.que[self.front])
#         if self.front==self.rare:
#             self.front=self.rare=-1
#         else:
#             self.front=(self.front+1)%self.size
            
#     def display(self):
#         if self.front==-1:
#             print("empty..")
#             return
#         print("Queue elements..")
#         print(self.que)
#         print("*********")
#         i=self.front
#         while True:
#             print(self.que[i],end="  ")
#             if i == self.rare:
#                 break
#             i=(i+1)%self.size
#         print()

# cq=CQ(5)
# cq.enqueue(10)
# cq.enqueue(20)
# cq.enqueue(30)
# cq.enqueue(40)
# cq.enqueue(50)
# cq.display()
# cq.dequeue()
# cq.dequeue()
# cq.display()
# cq.enqueue(300)
# cq.enqueue(400)
# cq.display()



# # #----------------------------------------------------------------------------->infix to postfix

# def precedence(op):
#     if op == '+' or op == '-':
#         return 1
#     if op == '*' or op == '/':
#         return 2
#     if op == '^':
#         return 3
#     return 0

# def isOperator(c):
#     return c in "+-*/^"

# def infixToPostfix(expression):
#     stack = []
#     result = ""

#     for char in expression:
       
#         if char.isalnum():
#             result += char

#         elif char == '(':
#             stack.append(char)
       
#         elif char == ')':
#             while stack and stack[-1] != '(':
#                 result += stack.pop()
#             stack.pop()
  
#         else:
#             while (stack and precedence(char) <= precedence(stack[-1])):
#                 result += stack.pop()
#             stack.append(char)
    
#     while stack:
#         result += stack.pop()

#     return result

# # exp = "(a*b)/(a+d)-e"
# # print("Postfix:", infixToPostfix(exp))



# #----------------------------------------------------------------------------------------> infix to prefix
# # 1 reverse stirng
# # 2 change brackets
# # 3 postfic
# # revrse ans string

# def infixToPrefix(s):
#     s=s[::-1]
#     temp = ""
#     for ch in s:
#         if ch == '(':
#             temp += ')'
#         elif ch == ')':
#             temp += '('
#         else:
#             temp += ch
#     ans=infixToPostfix(temp)
#     return ans[::-1]

# s = "(a*b)/(a+d)-e"
# print("Prefix:", infixToPrefix(s))


# #---------------------------------------------------------------->priority queue

# ### priority Queue ###
# class PriorityQueue:
#     def __init__(self):
#         self.que=[]
#     def enqueue(self,data,priority):
#         self.que.append((priority,data))
#         self.que.sort(key=lambda x:x[0])
        
#     def dequeue(self):
#         print(f"the poped element is {self.que.pop(0)[1]}")
        
    
#     def display(self):
#         print(self.que)
# p=PriorityQueue()
# p.enqueue(10,2)
# p.enqueue(70,1)
# p.enqueue(20,1)
# p.enqueue(30,3)
# # p.dequeue()
# p.display()



# #--------------------------------------------> Linear search

# def linearSearch(list,data):
#     for i in range(0,len(list)):
#         if list[i]==data:
#             return i
#     return -1

# def binarySearch(list,data):
#     start=0
#     end=len(list)-1
#     while start<=end:
#         mid=start+(end-start)//2
#         if(data<list[mid]):
#             end=mid-1
#         elif data>list[mid]:
#             start=mid+1
#         else:
#             return mid
#     return -1


# lst = [2, 4, 6, 8, 10, 12]
# key = 8
# pos = linearSearch(lst, key)
# if pos != -1:
#     print("Element found at index:", pos)
# else:
#     print("Element not found")


# def bubbleSort(list):
#     n=len(list)
#     for i in range (0,n):
#         for j in range (i,n-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list

# def selectionSort(list):
#     n=len(list)
#     for i in range (0,n):
#         minn=i
#         for j in range (i+1,n):
#             if list[minn]>list[j]:
#                 minn=j
#         list[i],list[minn]=list[minn],list[i]
#     return list



# def partition(arr,low,high):
#     pivot=arr[high]
#     i=low-1
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]

#     arr[i+1],arr[high]=arr[high],arr[i+1]
#     return i+1


# def quickSort(arr,low,high):
#     if low<high:
#         pi=partition(arr,low,high)
#         quickSort(arr,low,pi-1)
#         quickSort(arr,pi+1,high)

# def inserSort(list):
#     for i in range (1,len(list)):
#         for j in range (i,len(list)):
#             if list[j]<list[j-1]:
#                 list[j],list[j-1]=list[j-1],list[j]
#             else:
#                 break
#     return list

# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr

   
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])      
#     right = merge_sort(arr[mid:])     

#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0

 
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

    
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result


# arr = [2, 3, 10, 1, 22, 56]
# print("Sorted:", merge_sort(arr))




# lst = [2, 14, 6, 83, 10, 12]
# print(inserSort(lst))


# #---------------------------------------------------------> Recursion

# def printt(n):
#     if n==0:
#         return 0
#     printt(n-1)
#     print(n,end=" ")

# def printtt(n):
#     if n==0:
#         return 0
#     print(n,end=" ")
#     printtt(n-1)


# printt(5)
# print()
# printtt(5)

#----------------------------------> merge sort

def merge(list,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if list[left]<list[right]:
            temp.append(list[left])
            left+=1
        else:
            temp.append(list[right])
            right+=1
    while left<=mid:
        temp.append(list[left])
        left+=1
        
    while right<=high:
            temp.append(list[right])
            right+=1
    
    for i in range (len(temp)):
         list[low+i]=temp[i]
    

def mergeSort(list,low,high):
    if low==high:
        return
    mid=low+(high-low)//2
    mergeSort(list,low,mid)
    mergeSort(list,mid+1,high)
    merge(list,low,mid,high)


list=[1,56,2,45,6,3,32,34]
(mergeSort(list,0,7))
print(list)