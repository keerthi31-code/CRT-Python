'''
stack : it is a linear data structure ans it follows LIFO ex: bangles 
push & pop
push - inserting elements in to stack
pop- removing elements from stack

Implementation of stack 
'''
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop(0) # have to give the index
print(stack)
#peak - top most element -- can find using negative indexing -1
print(stack[-1])


stack=[]
def push(x):
    stack.append(x)
def pop():
    return stack.pop()
def peek():
    return stack[-1]

push(10)
push(20)
push(30)
print(stack)
print(pop())
print(peek())
#rev
stack=[1,2,3,4]
temp=[]
while stack:
    temp.append(stack.pop())
print(temp)
#product
stack=[2,3,4,5]
product=1
while stack:
    product=product*stack.pop()
print(product)

#minimum ele
stack=[10,5,8,2,6]
minimum=stack[0]
while stack:
    m=stack.pop()
    if m<minimum:
        minimum=m
print(minimum)

s='hello'
stack=[]
rev=''
for ch in s:
    stack.append(ch)
while stack:
    rev=rev+stack.pop()
print(rev)