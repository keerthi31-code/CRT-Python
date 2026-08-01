class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head is None:
            print("linked list is empty.")
            return
        temp=self.head
        while True:
            print(temp.data, end=" -> ")
            temp=temp.next
            if temp==self.head:
                break
    def insert_at_begin(self,data):
        new=node(data)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new
        new.next=self.head
        self.head=new
    def insert_at_end(self,data):
        new=node(data)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new
        new.next=self.head

    def insert_at_pos(self,data,pos):
        new=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new
    
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
cll=CLL()
cll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1
cll.Traversal()
cll.insert_at_begin(5)
cll.insert_at_end(45)
cll.insert_at_pos(23,3)
cll.Traversal()

