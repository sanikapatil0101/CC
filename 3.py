# ----------------------------------------------------------------detect fraud orders
# you are given a list of customer order a 1.
# customer comments fraud if they place more than 3 orders in one hour
#  2. all orders come from different device id 

# o=[
#  {"customer":"a","device":"d1","time":10},
#  {"customer":"a","device":"d2","time":10},
#  {"customer":"a","device":"d3","time":10},
#  {"customer":"a","device":"d4","time":10}
# ]
# track = {}
# fraud = set()
# for x in o:
#     key = (x["customer"], x["time"])
    
#     if key not in track:
#         track[key] = set()
    
#     track[key].add(x["device"])
    
#     if len(track[key]) > 3:  
#         fraud.add(x["customer"])
# print(list(fraud))


#-----------------------------------------------------------> file handeling

# ------------------------------------------------create x
# f=open("ex.txt","x")  

# -------------------------------------------------write w
# f=open("ex.txt","w")
# f.write("hi sanika...")
# f.close()

# --------------------------------------------------read r
# f=open("ex.txt","r")
# x=f.read()
# f.close()
# print(x)

#------------------------------------------------- append a
# f=open("ex.txt","a")
# f.write(" welcome here")
# f.close()
# f=open("ex.txt","r")
# print(f.read())
# f.close()

# -------------------------------------------------- write with read w+
# here req to set cursor at 0th location to write after read so need to us e-----------seek()

# f=open("ex.txt","w+")
# f.write(" byeeeeee")
# f.seek(0)
# print(f.read())
# f.close()

# f=open("ex.txt","w+")
# f.write("hello coders")
# f.seek(5,0)               # ---------------------seek(5,0) skip 5 from 0
# print(f.read())
# f.close()

# ---------------------------------------------------> appen with read a+
# f=open("ex.txt","a+")
# f.write("byeeeeee")
# f.seek(0)
# print(f.read())
# f.close()


# # read line ------------>return line
# f=open("ex.txt","r")
# print(f.readline())
# f.close()

# read lines ---------------> return lines in ---------- list
# f=open("ex.txt","r")
# print(f.readlines())
# f.close()

# f=open("ex.txt","r")     
# x=f.readlines()
# for i in x:
#     print(i)
# f.close()

# f=open("ex.txt","r")
# while x:=f.readline():           # ---- :=  operator neede
#     print(x)
# f.close()

# with open ("ex.txt","r") as f:      #---------no need t0 close file
#     x=f.read()
#     print(x)

# with open ("ex.txt","w+") as f:      #---------no need t0 close file and writelines
#     x=['hello sanika  ....','byee']
#     f.writelines(x)
#     f.seek(0)
#     print(f.read())

# ------------------------------------>binary file
# with open ("ex.bin","wb+") as f:
#     # x=b"sanika sunil patil"                     # ------------- b" " needed to convert binary 
#     #or
#     x="sanika sunil patil".encode("utf-8")      # ------------- .encode("utf-8")
#     f.write(x)
#     f.seek(0)
#     # print(f.read())
#     x=f.read()
#     print(x.decode("utf-8"))                       #.decode("utf-8")


# ---------------------------------------------------------------->os operations

# import os                                       #import library necessary
# os.rename("old.txt","new.txt")                #------------------> remane file name
# os.remove("new.txt")                          #------------------> remove file
# os.makedirs("abcd")                           #------------------> make directory only one
# os.mkdir("pqrs")                              #------------------> make directory folders and subfolders
# print(os.getcwd())                            #------------------> get cirrent working directory
# print(os.listdir("D:\\"))                     #------------------> list directory from specific driev as list
# for i in os.listdir():                        #------------------> list directory from specific driev from list
#     print(i)
# print(os.cdir("D:\\"))                        #------------------> change directory                     
# os.rmdir("pqrs")                              #------------------> remove directory


# split()                                       string -> list
# join()                                        list -> string
# s=["hello","students","welcome"]
# d="~".join(s)
# d=" ".join(s)
# print(d)

# l=['p','y','t','h','o','n']
# print("".join(l))

# l=("1","2","3","4")
# print("-".join(l))

# l={"maggie","pizza","pavbhaji"}
# print(",".join(l))
# print("\n".join(l))

# d={"a":"1","b":"2","c":"3"}
# print(" ".join(d))
# print(" ".join(d.values()))

# l=[1,2,3,4,5]
# print(",".join(list(map(lambda i:str(i),l))))

# s="hello"
# print("-".join(s))

# l=[[1,2],[3,4],[5,6]]
# print(",".join([str(j) for i in l for j in i]))
# print(",".join(",".join(map(str,i))for i in l))

# l=["python","is","fun"]
# l.reverse()
# l=l[::-1]
# print(",".join(l[::-1]))
# print(",".join(reversed(l)))

# ch=["A","B","C"]
# print(",".join(str(ord(i)) for i in ch))               #-------------------> to obatin ASCII ord() require

# s = "beautiful"
# print("-".join(c for c in s if c in "aeiou"))


# table=[["name","age","city"],
#       ["raj","25","Nashik"],
#       ["amit","30","pune"]]


# #-------------------------------------------------------------> enumerate
# l=[10,25,30,41,55]
# for i,v in enumerate(l):
#     if v%2==0:
#         print(i,v)

# l=["a","b","c"]
# print(list(enumerate(l)))

# l=[5,10,15]
# # print(list(map(lambda i:i*2,l)))
# for i,v in enumerate(l):
#     l[i]=v*2
# print(l)

# s="cat"
# print(set(enumerate(s)))

# l=[[10,20],[30,40],[50,60]]
# for i,v in enumerate (l):
#     print(i," ".join(str(j) for j in v))

# c=["red","blue","green","yellow"]
# s="green"
# for i,v in enumerate(c):
#     print(f"found {v} at {i}" if v==s else f"{s} not found")

# for i,v in enumerate(c):
#     print(i,":",v)

# ------------------------------------------------->exception handeling

# # -----------------------> 1 ZeroDivisionError
# x=10
# y=0
# print(x/y)

# # ----------------------> 2 TypeError
# x=10
# y="hi"
# print(x/y)

# --------------------------> try except

# try:
#     n1 = int(input())
#     n2 = int(input())
#     ans = n1 / n2
#     print(ans)

# # except ZeroDivisionError:
# #     print("failed to divide")
# # except ValueError:
# #     print("invalid input")
# except Exception as p:
#     print("other error:", p)

# # except (ZeroDivisionError,ValueError):
# #     print("failed to divide")

# print("hi")


# try:
#     n1 = int(input())
#     n2 = int(input())
#     ans = n1 / n2
#     print(ans)

# # except ZeroDivisionError:
# #     print("failed to divide")

# except ZeroDivisionError as e:
#     print(e.__class__,e)

# else:                              #if excepttion not occure then only print
#     print("from else")

# finally:                           #every time print
#     print("from finally")


# age =int(input("enter age:"))
# try:
#   if age<0:
#      raise ValueError("here msg for you..:age is invalid")
#   print("age is:",age)
# except ValueError as e:
#    print(e)
# print("remianing line of code")



class percentagegreaterThan100(Exception):
   def __init__(self,x="exception occurs cause per"):
      super().__init__(self,x)

per=float(input("enter percentage:"))
try:
   if per>100:
      raise percentagegreaterThan100
except percentagegreaterThan100 as e:
      print(e)



