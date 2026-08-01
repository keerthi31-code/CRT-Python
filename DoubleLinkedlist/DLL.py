class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def Traversal(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    #reverse traversing
    def reverse_ele(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print("rev:",temp.data)
            temp=temp.prev
    def insert_ele_begin(self,data):
        new=node(data)
        new.next=self.head
        self.head.prev=new
        self.head=new
    def insert_at_end(self,data):
        new=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp 
    def insert_at_pos(self,data,pos):
        new=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next.prev=new
        new.prev=temp
        temp.next=new
    def del_at_begin(self):
        temp=self.head
        self.head=temp.next
        self.head.prev=None
    def del_at_end(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
    def del_at_pos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev





n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
dll=DLL()
dll.head=n1
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3

dll.Traversal()
dll.reverse_ele()
dll.Traversal()
dll.insert_ele_begin(0)
dll.Traversal()
dll.insert_at_end(5)
dll.Traversal()
dll.insert_at_pos(22,2)
dll.Traversal()
dll.del_at_begin()
dll.Traversal
dll.del_at_end()
dll.Traversal()
dll.del_at_pos(4)
dll.Traversal()




