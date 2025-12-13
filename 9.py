#-------------------------------------------> Binary Search Tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None  
         
class BST:
    def insertNode(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left=self.insertNode(root.left,data)
        else:
            root.right=self.insertNode(root.right,data)
        return root        
    
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
                
    def findmin(self,root):
        r=root
        while r.left:
            r=r.left
        return r
                
    def findmax(self,root):
        r=root
        while r.right:
            r=r.right
        return r
    
    def deleteNode(self,root,key):
        if root is None:
            return root

        if key < root.data:
            root.left=self.deleteNode(root.left,key)
        elif key> root.data:
            root.right=self.deleteNode(root.right,key)
            
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp=self.findmin(root.right)
            root.data=temp.data
            root.right=self.deleteNode(root.right,temp.data)
            
        return root 
    
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    
    def countLeaf(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeaf(root.left) + self.countLeaf(root.right)


    def countNonLeaf(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1 + self.countNonLeaf(root.left) + self.countNonLeaf(root.right)

    def diameter(self,root):
        if root is None:
            return 0
        through=self.height(root.left)+self.height(root.right)
        left_dia = self.diameter(root.left)
        right_dia = self.diameter(root.right)
        return max(through, left_dia, right_dia)


    def count_2childNode(self, root):
        if root is None:
            return 0

        left = self.count_2childNode(root.left)
        right = self.count_2childNode(root.right)

        if root.left is not None and root.right is not None:
            return 1 + left + right
        else:
            return left + right

    
        
root=None 
b=BST()              
root=b.insertNode(root,100)
root=b.insertNode(root,120)
root=b.insertNode(root,90)
root=b.insertNode(root,56)
root=b.insertNode(root,78)
root=b.insertNode(root,123)
root=b.insertNode(root,111)
root=b.insertNode(root,130)
root=b.insertNode(root,45)
root=b.insertNode(root,95)
b.LOT(root)
root=b.deleteNode(root,100)
print("...")
b.LOT(root)
print("...")
print(b.count_2childNode(root))