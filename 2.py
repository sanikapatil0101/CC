# day 2

# l=[101,205,101,333,205]
# l1=[]
# for x in l:
#    if x in l1:
#        continue
#    else:
#        l1.append(x)
# print(l1)


# l=["apple","banana","apple","orange","orange","orange"]

# dict={}
# for x in l:
#     if x in dict:
#         dict[x]+=1
#     else:
#         dict[x]=1
# print(dict)


# a,b,*c=(1,2,3,4)
# print(c)


# l=[2,34,12,4,56,54,56,2,67233,78,17,9,68]
# for i in range(len(l)//2):
#     l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
# print(l)


# merge sorted list
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = []
# i = 0
# j = 0
# while i < len(l1) and j < len(l2):
#     if l1[i] < l2[j]:
#         l3.append(l1[i])
#         i += 1
#     else:
#         l3.append(l2[j])
#         j += 1

# while i < len(l1):
#     l3.append(l1[i])
#     i += 1

# while j < len(l2):
#     l3.append(l2[j])
#     j += 1

# print(l3)



# find longest increasing subsequence length
# l=[10,22,9,33,21,50,60]
# l1=1
# for i in range(1,len(l)):
#     if(l[i-1]>l[i]):
#         l1=1
#     else:
#         l1+=1
# print(l1)


# replace all ocerence of x with y
# l=[1,2,1,3,1] 
# replace 1 with 9
# for i in range(len(l)):
#     if l[i]==1:
#         l[i]=9
# print(l)


# l1 =[1 ,5 ,10]
# l2 =[5,10,20]
# l3=[10,20]
# l4=[]
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         for k in range(len(l3)):
#             if l1[i]==l2[j] and l2[j]==l3[k]:
#                 l4.append(l1[i])
# for x in l1:
#     if x in l2 and x in l3:
#         l4.append(x)
# print(l4)


# reaarane list such that postive come before neg
# l=[1,-2,3,-4,5]
# l=[x for x in l if x >= 0]+[x for x in l if x < 0]
# print(l)


# find kth largest element in list
# k1=int(input())
# l=[10,4,3,50,23]
# k=0
# while k<len(l):
#     mx=l[k]
#     c=k
#     for i in range(k,len(l)):
#         if l[i]>mx:
#             mx=l[i]
#             c=i
#     l[c],l[k]=l[k],l[c]
#     k+=1
# print(l[k1-1])


# type hint
# def fun():
#     """def add(a:int,b:int)->int:
#         return a+b
#     print(add(4,7.8))"""
# print(fun.__doc__)


# def add(a:int,b:int)->int:
#         return a+b
# print(add(4,7.8))
# print(add.__annotations__)


# annonomous function
# sq=lambda x: x**2 
# print(sq(5))

# print((lambda x:x**2)(5))

# sq=lambda x: x**3 
# print(sq(5))

# print((lambda x:x**3)(5))


# filter

# def isev(n):
#     if n%2==0:
#         return n
# l=[1,2,3,4,5,6]
# print(list(filter(isev,l)))

# l=['2','5','7']
# d=[]
# for i in l:
#     d.append((lambda i:int(i))(i))
# print(d)

# x=5
# print((lambda x:x+10)(x))
# print((lambda x:x%2==0)(x))
# print((lambda x,y:x if x>y else y)(2,3))


# higher ordered function

# def sq(x):
#     return x*x

# def applysq(fun,value):
#     return fun(value)

# print(applysq(sq,5))


# def outer():
#     def inner():
#         return "hi"
#     return inner
# f=outer()
# print(f())


# map
# nums=[1,2,3,4,5]
# def sq(r):
#     return r*r
# d=list(map(sq,nums))
# print(d)

# l=[10,20,30]
# def add(n):
#     return n+1
# print(list(map(add,l)))

# l=["10","20","30"]
# print(list(map(lambda i:int(i),l)))
# print(list(map(int,l)))

# l=["maggie","pizza","burger","faculty"]
# print(list(map(lambda i:i.upper(),l)))

# l1=[1,2,3]
# l2=[10,20,30]
# print(list(map(lambda x,y:x+y,l1,l2)))

# l1=['a','b','c']
# l2=['x','y','z','p','q']
# print(list(map(lambda x,y:x+y,l1,l2)))

# d={"a":"1","b":"2"}
# print(dict(map(lambda kv:(kv[0],int(kv[1])),d.items())))

# l=["hello unnati mam","strict teacher"," hello teacher"]
# print(list(map(lambda x:len(x),l)))
# print(list(map(lambda x:len(x.split()),l)))


# x=5.3243
# print(f"{x:.2f}")

# l=[1.4332,67.2323,99.98767,67.09]
# print(list(map(lambda x:f"{x:.2f}",l)))

# l = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x*x, filter(lambda x: x%2==0,l))))

# l=[" 5 "," raj ",' 94 ']
# print(list(map(lambda x:int(x),filter(lambda x:x.strip().isdigit(),l))))

# remove falsy values
# l=[1,0.0,None,"Raj",0,6]
# print(list(filter(bool,l)))

# l=["madam","racecar","see","hello","level"]
# print(list(filter(lambda x:x==x[::-1],l)))
# print(list(filter(lambda x: len(x) > 3, l)))


#prime number :1 to 21

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# for x in range(1,21):
#     if is_prime(x):
#         print(x,end=" ")

# l=[5,6,7,10,11,20]
# print(list(filter(lambda x:x%5==0,l)))

# l=["apple","om","jay","Akash","ajay"]
# print(list(filter(lambda x: x[0]=='a',map(lambda x:x.lower(),l))))

#filter floats that have an even last digit after decimal
# l=[12.34,45.67,89.123,7.456,3.1416,10.28]
# print(list(filter(lambda x: int(str(x).split('.')[-1][-1]) % 2 == 0, l)))

l=["enlist","silent","apple","tensile","stone"]
d="listen"
print(list(filter(lambda x: sorted(d)==sorted(x),l)))







    
