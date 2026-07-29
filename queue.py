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
