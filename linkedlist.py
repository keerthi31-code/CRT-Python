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
    def Traversal(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            temp=self.head
            while temp:
                print(temp.data, end="-> ")
                temp=temp.next
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
sll.Traversal()

