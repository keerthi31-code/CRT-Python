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


