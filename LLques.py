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
    def sum_of_nodes(self):
            temp=self.head
            sum=0
            while temp is not None:
                sum+=temp.data
                temp=temp.next
            print("sum of nodes=",sum)
   
    def count_of_nodes(self):
            temp=self.head
            count=0
            while temp:
                count+=1
                temp=temp.next
            print("count of node:",count)

    def even_elements(self):
        temp=self.head
        total=0
        while temp:
            if temp.data%2==0:
                total+=temp.data
            temp=temp.next
        print("sum of even elements:",total)

    def sum_of_evenNodes(self):
        temp=self.head
        pos=1
        total=0
        while temp:
            if pos%2==0:
                total+=temp.data
            pos+=1
            temp=temp.next
        print("sum of even nodes:",total)

    def search_element(self,val):
        temp=self.head
        while temp:
            if temp.data==val:
                return True
            temp=temp.next
        return False
    
    def max_element(self):
        temp=self.head
        max1=self.head.data
        while temp:
            if temp.data >= max1:
                max1=temp.data
            temp=temp.next
        return max1

n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)
sll=SLL()
sll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
sll.Traversal()
sll.sum_of_nodes()
sll.count_of_nodes()
sll.even_elements()
sll.sum_of_evenNodes()
print(sll.search_element(7))
print(sll.max_element())


