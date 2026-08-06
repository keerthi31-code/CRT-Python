m=[]
v=3
graph=[[0 for i in range(v)] for j in range(v)]
graph[0][1]=1
graph[1][0]=1
graph[0][2]=1
graph[2][0]=1
graph[1][2]=1
graph[2][1]=1
for m in graph:
    print(m)

#dict 
# graph={}
# def add_edge(u,v):
#     if u not in graph:
#         graph[u]=[]
#     if v not in graph:
#         graph[v]=[]
#     graph[u].append(v)
#     graph[v].append(u)
# add_edge('A','B')

# Traversing 
#BFS -- Breadth first Search
'''
         A
        / \        |A|B|C|D|E|F|
        B  C        it follows the queue 
       / \  \       popped element add to the list
       D  E  F      
'''
from collections import deque
def bfs(graph, start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        vertex=queue.popleft()
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(vertex)
                queue.append(neighbour)
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B'],
    'F':['C']
}

bfs(graph,'A')


#DFS


def dfs(graph,start):
    visited=set()
    stack=[start]
    visited. add(start)
    while stack:
        vertex=stack.pop()
        print(vertex,end=" ")
        for neighbour in reversed(graph[vertex]):
            if neighbour not in visited:
                stack.append(neighbour)
                visited.neighbour(stack)
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B'],
    'F':['C']
}
visited=set()
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)
dfs('A')