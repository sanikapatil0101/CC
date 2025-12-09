#--------------------------------------------------------> Recursion <----------------------------------------

# interative take less time 
# recursion takes more time 
# types of recursion:
# 1 top down approch  (n=5            5 4 3 2 1)
# 2 bottom up approch (n=5 (i=0)      1 2 3 4 5) 
# (head recursion)                    (recursion function at first)
# (tail recursion)                    (recursion function at last)

# #--------------------------------------------------factorial - top down

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# #--------------------------------------------------factorial - bottom up

# def fact(n,i=1):
#     if i==n:
#         return n
#     return i*fact(n,i+1)
# print(fact(5))


# fibonacci bottom up

# def fib(n,l=[0,1],i=2):
#     if n==0:
#         return [0]
#     if n==1:
#         return [0,1]
#     if i>n:
#         return l
#     l.append(l[-1]+l[-2])
#     return fib(n,l,i+1)

# def fib(n,l=[0,1]):
#     if len(l)>n:
#         return l
#     l.append(l[-1]+l[-2])
#     return fib(n,l)
# print(fib(10))

# def summ(n):
#     if n==0:
#         return 0
#     return n+summ(n-1)
# print(summ(5))


# def ispal(s,i=0,j=None):
#     if j is None:
#       j=len(s)-1
#     if i>=j:
#         return True
#     if s[i]!=s[j]:
#         return False
#     return ispal(s,i+1,j-1)

# s="saaaaaas"  
# print(ispal(s))


# #sum of digits
# def summ(n):
#     if n==0:
#         return 0
#     return (n%10)+summ(n//10)
# print(summ(123))



# def ispal(s,i=0,j=None):
#     if j is None:
#       j=len(s)-1
#     if i>=j:
#         return True
#     if s[i]!=s[j]:
#         return False
#     return ispal(s,i+1,j-1)



#1.reverse string
#top-down
# def revs(s):
#     if s == "":
#         return ""
#     return revs(s[1:]) + s[0]
# print(revs("Train"))


#bottom-up
# def revs(s, i=0):
#     if i == len(s):
#         return ""
#     return revs(s, i+1) + s[i]
# print(revs("train"))






#2.power
#top-down
# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b-1)
# print(power(2,3))


#bottom-up
# def power(a, b, i=0, ans=1):
#     if i == b:
#         return ans
#     return power(a, b, i+1, ans*a)
# print(power(2,3))






#3.find max in array
#top-down
# def maxt(arr, n):
#     if n == 1:
#         return arr[0]
#     return max(arr[n-1], maxt(arr, n-1))
# arr=[2,4,67,6,8]
# print(maxt(arr,4))


#bottom-up
# def max_bottom(arr, i=0, maxi=None):
#     if maxi==None:
#         maxi=arr[0]   
#     if i == len(arr):
#         return maxi
#     return max_bottom(arr, i+1, max(maxi, arr[i]))

# print(max_bottom([2,5,1,9,3]))





#4.find minimum in array
#top-down
# def mint(arr, n):
#     if n == 1:
#         return arr[0]
#     return min(arr[n-1], mint(arr, n-1))

# print(mint([2,5,1,9,3], 5))



#bottom-up
# def min_bottom(arr, i=0, mini=None):
#     if mini==None:
#         mini=arr[i]
#     if i == len(arr):
#         return mini
#     return min_bottom(arr, i+1, min(mini, arr[i]))

# print(min_bottom([2,5,1,9,3]))







#5.count zeroes in number
#top-down
# def count_zero_top(n):
#     if n == 0:
#         return 1
#     if n < 10:
#         return 0
#     return (1 if n % 10 == 0 else 0) + count_zero_top(n//10)

# print(count_zero_top(102030))



#bottom up
# def count_zero_bottom(n, c=0):
#     if n == 0:
#         return c+1 if c==0 else c
#     if n < 10:
#         return c
#     return count_zero_bottom(n//10, c + (1 if n % 10 == 0 else 0))

# print(count_zero_bottom(102030))




#6. Multiply Without Using *
#top down
# def mul_top(a, b):
#     if b == 0:
#         return 0
#     return a + mul_top(a, b-1)

# print(mul_top(2, 3))


#bottom up
# def mul_bottom(a, b, i=0, ans=0):
#     if i == b:
#         return ans
#     return mul_bottom(a, b, i+1, ans+a)

# print(mul_bottom(2, 3))

#7.check if array is sorted
#top down
# def sortp(arr, i=0):
#     if i == len(arr)-1:
#         return True
#     return arr[i] <= arr[i+1] and sortp(arr, i+1)

# print(sortp([1,2,3,4,5]))


#bottom up
# def sortb(arr, i=None):
#     if i is None:
#         i = len(arr)-1
#     if i == 0:
#         return True
#     return arr[i-1] <= arr[i] and sortb(arr, i-1)

# print(sortb([1,2,3,4,5]))





#8.binary search
#top down
# def bs(arr, key, l, r):
#     if l > r:
#         return -1
#     mid = (l+r)//2
#     if arr[mid] == key:
#         return mid
#     if key < arr[mid]:
#         return bs(arr, key, l, mid-1)
#     return bs(arr, key, mid+1, r)

# print(bs([1,2,3,4,5,6], 4, 0, 5))


#bottom up
# def bsb(arr, key, l, r):
#     if l > r:
#         return -1
#     mid = (l+r)//2
#     if arr[mid] == key:
#         return mid
#     return bsb(arr, key, l, mid-1) if key < arr[mid] else bsb(arr, key, mid+1, r)

# print(bsb([1,2,3,4,5,6], 4, 0, 5))





#9. Linear Search
#top-down
# def lst(arr, key, i=0):
#     if i == len(arr):
#         return -1
#     if arr[i] == key:
#         return i
#     return lst(arr, key, i+1)

# print(lst([10,20,30,40], 30))


#bottom-up
# def lst(arr, key, i=None):
#     if i is None:
#         i = len(arr)-1
#     if i < 0:
#         return -1
#     if arr[i] == key:
#         return i
#     return lst(arr, key, i-1)

# print(lst([10,20,30,40], 30))




















#-----------------------------------------------------> TREE

class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
from collections import deque

def levelTraverse(root):
    if not root:
        return []
    
    ans=deque()
    ans.append(root)

    while ans:
        curr=ans.popleft()
        print(curr.data,end=" ")
        if curr.left :
            ans.append(curr.left)
        if curr.right :
            ans.append(curr.right)
    
    print()

# def inorderTraversal(root):
#     if root is not None:
#         inorderTraversal(root.left)
#         print(root.data,end=" ")
#         inorderTraversal(root.right)

# def preorderTraversal(root):
#     if root is not None:
#         print(root.data,end=" ")
#         preorderTraversal(root.left)
#         preorderTraversal(root.right)

# def postorderTraversal(root):
#     if root is not None:
#         postorderTraversal(root.left)
#         postorderTraversal(root.right)
#         print(root.data,end=" ")
    
def inorderTraversal(root):
    if root is None:
        return []
    s=[]
    curr=root
    while curr or s:
        while curr:
            s.append(curr)
            curr=curr.left
        curr=s.pop()
        print(curr.data,end=" ")
        curr=curr.right

def preorderTraversal(root):
    if root is None:
        return
    stack=[root]
    while stack:
        n=stack.pop()
        print(n.data,end=" ")
        if n.right: stack.append(n.right)  
        if n.left: stack.append(n.left)   

def postorderTraversal(root):
    if root is None:
        return
    s1=[root]
    s2=[]
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:  s1.append(node.left)
        if node.right: s1.append(node.right)
    while s2:
        print(s2.pop().data,end=" ")
 



root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
root.left.left.left=node(8)
root.left.left.right=node(9)
root.left.right.left=node(10)
levelTraverse(root)
inorderTraversal(root)
print()
preorderTraversal(root)
print()
postorderTraversal(root)
print()


