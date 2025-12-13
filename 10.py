class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
        
class AVL:
    def insert(self,root,data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
            
        root.height=max(self.getheight(root.left),self.getheight(root.right))+1
        bf=self.balancefactor(root)
        
        #LL: right
        if bf > 1 and data < root.left.data:
            return self.rightrotate(root)
        
        #RR: left
        if bf < -1 and data > root.right.data:
            return self.leftrotate(root)        
        
        #LR  : left then right
        if bf > 1 and data > root.left.data:
            root.left=self.leftrotate(root.left)
            return self.rightrotate(root)
    
        #RL : right then left
        if bf < -1 and data < root.right.data:
            root.right=self.rightrotate(root.right)
            return self.leftrotate(root)
        return root
    
    def getheight(self,root):
        if not root:
            return 0
        return root.height
    def balancefactor(self,root):
        if not root:
            return 0
        return self.getheight(root.left)-self.getheight(root.right)
    
    def leftrotate(self,a):                         
        b=a.right
        b.left=a
        a.right=None
        a.height=max(self.getheight(a.left),self.getheight(a.right))+1
        b.height=max(self.getheight(b.left),self.getheight(b.right))+1

        return b
    
    def rightrotate(self,a):
        b=a.left
        b.right=a
        a.left=None
        a.height=max(self.getheight(a.left),self.getheight(a.right))+1
        b.height=max(self.getheight(b.left),self.getheight(b.right))+1
        return b
    
        
    
    def LOT(self,root):
        if root is None:
            return 
        que=[]
        que.append(root)
        while que:
            curr=que.pop(0)
            print(curr.data,end=" ")
            if curr.left:
                que.append(curr.left)
            if curr. right:
                que.append(curr.right)
    
    
    
root=None
a=AVL()
root=a.insert(root,10)
root=a.insert(root,20)
root=a.insert(root,15)
a.LOT(root)









class TrieNode:
    def __init__(self):
        self.child={}
        self.eow=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        r=self.root
        for i in word:
            if i not in r.child:
                r.child[i]=TrieNode()
            r=r.child[i]
        r.eow=True
        
    def search(self,word):
        r=self.root
        for i in word:
            if i not in r.child:
                return False
            r=r.child[i]
        return r.eow
    def startswith(self,s):
        r=self.root
        for i in s:
            if i not in r.child:
                return False
            
            r=r.child[i]
        return True
    def delete(self,word):
        r=self.root
        for i in word:
            if i not in r.child:
                return False
            r=r.child[i]
        r.eow=False
        return r.eow
        
    
t=Trie()
t.insert("do")
t.insert("done")
t.insert("does")
# print(t.search("dont"))
# print(t.startswith("d"))
t.delete("do")
print(t.search("do"))



















# direct addressing

class directaddressing:
    def __init__(self,size):
        self.table=[None]*size
        
    def insert(self,key,value):
        self.table[key]=value
        
    def search(self,key):
        return self.table[key]
    
    def delete(self,key):
        self.table[key]=None
        
dt=directaddressing(10)
dt.insert(2,"Unnati")
dt.insert(6,"Rahul")
dt.insert(7,"raj")
dt.insert(7,"rajvardhan")
print(dt.search(5))
print(dt.search(6))
dt.delete(6)
print(dt.search(7))





# hashing with chaining
class hashingwithchaining:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
        
    def hashfunction(self,key):
        return key % self.size
        
    def insert(self,key,value):
        index=self.hashfunction(key)
        for i in self.table[index]:
            if i[0]==key:
                i[i]=value
                return
        self.table[index].append([key,value])
 
 
    def search(self,key):
        index=self.hashfunction(key)
        for i in self.table[index]:
            if i[0]==key:
                return i[1]
        return None
    
h=hashingwithchaining(7)
h.insert(2,"apple")
h.insert(16,"banana")
print(h.search(16))





