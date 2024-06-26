


class BinarySearchTreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

    def add_child(self, data):
        if self.data==data: return

        if data<self.data:
            if not self.left:
                self.left = BinarySearchTreeNode(data)
            else:
                self.left.add_child(data)
        else: #data>self.data            
            if not self.right:
                self.right = BinarySearchTreeNode(data)
            else:
                self.right.add_child(data)
    def preorder(self):
        elems = []
        elems.append(self.data) 
        if self.left:
            elems += self.left.preorder()
        if self.right:
            elems += self.right.preorder()
        return elems 
    def inorder(self):
        elems = []
        if self.left:
            elems += self.left.inorder()
        elems.append(self.data)
        if self.right:
            elems += self.right.inorder()
        return elems         
    def postorder(self):
        elems = []
        if self.left:
            elems += self.left.postorder()
        if self.right:
            elems += self.right.postorder()
        elems.append(self.data)    
        return elems    
    def search(self, data):
        if self.data==data: return True

        if data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False                     
    def find_min(self):
        if self.left:
            return self.left.find_min()     
        else:
            return self.data   
        
    def find_max(self):
        if self.right:
            return self.right.find_max()     
        else:
            return self.data             
    def calculate_sum(self):
        sum=0
        if self.left:
            sum+=self.left.calculate_sum()
        sum+=self.data    
        if self.right:
            sum+=self.right.calculate_sum()
        return sum

    

def buildtree(elems):
    root = BinarySearchTreeNode(elems[0])
    for e in elems[1:]:
        root.add_child(e)
    return root    

ll = [3,5,8,5,2,6,7]
tt = buildtree(ll)
print(tt.inorder())
print(tt.search(6))
print(tt.search(9))
print(tt.find_max())
print(tt.find_min())
print(tt.calculate_sum())
print(tt.preorder())
print(tt.postorder())