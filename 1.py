# l=(10,8)
# print(id(l))
# l=l+(40,)
# print(id(l))
# print(l)

# name,id=input("enter ").split()
# print("name ",name , "id ", id)

# x="sanika"

# print(x.center(len(x)+8,"t")+"jjj")

# print(x.capitalize())

# x=10
# while x<=20:
#  print("h")
#  x+=1
# else:
#  print("he")


# a=[]
# x=1
# while(1):
#     if(x<6):
#         a.append(x)
#         x+=1
    
#     else:
#         break
# print(a)

# while(x<=10):
#     if(x==5):
#         x+=1
#         continue
#     else:
#         print(x,end=" ")
#         x+=1

# for i in range (10):
#     print(i+1,end=" ")

# student={
#     "id":1,
#     "name":"sanika",
#     "age":19,
#     "sub":["s1","s2"]
# }

# for i in student.values():
#     print (i) 

# student['per']=100

# for i in student:
#     print (i,student[i]) 

# print(student["per"])

# print(student.get("per"))

# print(student.get("per","no key exist"))

# x = [10, 20, 10, 40, 30, 40]

# freq = {}          

# for num in x:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# dupl = []
# uni= []

# for key in freq:
#     if freq[key] > 1:
#         dupl.append(key)
#     uni.append(key)

# print("Duplicates:", dupl)
# print("Unique number list:", uni)

# d=[]
# nx=[]

# for i in x:
#     if i in nx:
#         d.append(i)
#     else:
#         nx.append(i)

# print(d)
# print(nx)



# x=[33,4,23,213,1,43,283,123]
# mn=x[0]
# mx=x[0]

# for i in x:
#     if(i>mx):
#         mx=i
#     elif i<mn:
#         mn=i

# print(mn,mx)


# x=27
# print("adult") if x>=18 else print("child") 

# x=90
# print("odd") if x%2==1 else print ("even")

# x=0
# print("negative") if x<0 else print ("positive") if x>0 else print ("zero")

# l=[]
# i=0
# while i<10:
#     k=(i+1)**2
#     l.append(k)
#     i+=1
# print(l)

#walrus operatot
# print(l:=[i**2 for i in range (1,11)])


# print(l:=[i for i in range (1,21) if i%2==0])


# fruits=["apple","banana","pineapple","watermelon"]
# # print(l:=[len(i) for i in fruits])
# print([i[0] for i in fruits])

# print([i**2 if i % 2 == 0 else i**3 for i in range(1, 21)])

# print([[i for i in range (1,4)]for j in range (1,4)])


# print({i:i*2 for i in range (1,11)})


# print({i:"odd" if i%2==1 else "even" for i in range(1,21)})

# l=[10,"abc",7,3.5,9]
# print([i for i in l if type(i)==int])

# l=["madam","cat","dog","mom","racecar"]
# print([i for i in l if i==i[::-1]])

# l=[[1,2],[3,4]]
# print([j for i in l for j in i ])


# l=[2,4,7,9,5,3]

# k=0
# while k<len(l):
#     mx=l[k]
#     c=k
#     for i in range(k,len(l)):
#         if l[i]>mx:
#             mx=l[i]
#             c=i
#     # temp=l[k]
#     l[c],l[k]=l[k],l[c]
#     # l[c]=temp
#     k+=1
# print(l)

# print("second largest number is",l[1])

# # print([l[i]+l[len(l)-i-1] if len(l)%2==0 else l[i+1] for i in range (0,len(l)//2)])

# p=[]
# for i in range (0,len(l)//2):
#     p.append(l[i]+l[len(l)-i-1])
# if len(l)%2==1:
#     p.append(l[len(l)//2])
# print(p)


