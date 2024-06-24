#I will implement a LinkedList class myself

class Node():
    def __init__(self, value=None, next=None) -> None:
        self.val = value
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head=None
    
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr = itr.next
        return count
        
    def addbegin(self, val):
        newnode = Node(val, self.head)
        self.head = newnode

    def add(self, val):
        if self.head==None:
            self.head = Node(val)
        else:
            itr = self.head
            while itr.next:
                itr=itr.next                
            itr.next = Node(val)

    def printme(self):
        if not self.head:
            print('Empty')
        else:
            itr=self.head
            res=[]
            while itr:
                res.append(itr.val)  
                itr=itr.next   
            print(res)

    def insert_at(self, val, idx):
        if idx<=0: 
            self.addbegin(val)
            return
        itr=self.head
        for i in range(idx-1):
            itr=itr.next
        newnode=Node(val,itr.next.next)
        itr.next=newnode

    def remove_at(self, idx):
        if idx <= 0:
            self.head = self.head.next
            return 
        
        count=0
        itr=self.head
        while itr:
            if count == idx-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
        else:    
            print('Index out of bounds')

    def addlist(self, vals):
        #find tail
        itr=self.head
        if itr:
            while itr.next:
                itr = itr.next
        else:
            self.head=Node(vals[0])
            vals=vals[1:]

        #add list to tail
        for val in vals:
            itr.next=Node(val)
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr=self.head
        while itr:
            if itr.val==data_after:
                newnode=Node(data_to_insert, itr.next)
                itr.next=newnode
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr=self.head
        if itr.next==None:
            self.head=None
            return
        
        if itr.val==data:
            self.head=itr.next
            return

        while itr.next:
            if itr.next.val==data:
               itr.next=itr.next.next
               return
            itr = itr.next

ll = LinkedList()
ll.printme()
ll.add(10)
ll.add(60)
ll.add(30)
ll.add(40)
ll.add(20)
ll.printme()                
ll.insert_at(100,2)
ll.printme()
print(ll.length())
ll.remove_at(3)
ll.printme()
print(ll.length())
ll.addlist([33,22,11,29])
ll.printme()
ll.insert_after_value(22,900)
ll.printme()
ll.remove_by_value(900)
ll.printme()
ll.remove_by_value(29)
ll.printme()