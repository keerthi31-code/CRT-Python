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
graph={}
def add_edge(u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[u].append(v)
    graph[v].append(u)
add_edge('A','B')

# Traversing 
#BFS -- Breadth first Search
'''
         A
        / \        |A|B|C|D|E|F|
        B  C
       / \  \
       D  E  F
'''


