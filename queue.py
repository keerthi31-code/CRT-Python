queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print(queue.pop(0))


from collections import deque
queue=deque()
#enqueue
queue.append(10)
queue.append(20)
print(queue)
print(queue.popleft())


queue=deque([1,2,3,4,5])
k=3
stack=[]
for i in range(k):
    stack.append(queue.popleft())
while stack:
    queue.append(stack.pop())
for i in range(len(queue)-k):
    queue.append(queue.popleft())
print(queue)

