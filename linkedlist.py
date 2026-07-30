class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
temp=n1
while temp:
    print(temp.data)
    temp=temp.next


    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_at_begin(self, data):
        new=node(data)
        new.next=self.head
        self.head=new
    def insert_at_end(self, data):
        new=node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new      
    def Traversal(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            temp=self.head
            while temp:
                print(temp.data, end="-> ")
                temp=temp.next
new=node(5)
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
sll=SLL()
sll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
sll.insert_at_begin(5)
sll.insert_at_end(60)

sll.Traversal()

