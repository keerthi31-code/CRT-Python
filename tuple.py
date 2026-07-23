# tuple is collection of items that is oederd, immutable, allows duplicates
t=(10,20,30,40,20)
print(t)

t=(10,20,30.5,40,20,'rani')
print(t)
#dynamic input
#t=tuple(map(int,input().split()))
#print(t)


t=(2,4,5,6)
print(t[0])
print(t[2])
print([-1])
print([-3])

t=(10,20,30,10)
print("count:",t.count(10))
print("index:",t.index(10))

t=(10,20,30)
print(list(t))
print(set(t))
print(tuple(t))


t=(10,20,30)
t1=(40,50,60)
print(t+t1)
print(t*2)
print(t1*3) # 3 tyms repeation

t=(10,20,30)
for i in t:
    print(i)

#nested tuple 
t=((1,2,3),(4,5))
print(t)


'''t=((1,2,3),(3,4))
o/p:13
t=(2,3,4,5,6,7,8,9,10,11)
o/p:(2,3,5,7,11)
'''

t=((1,2,3),(3,4))
sum=0
for i in t:
    for j in i:
        sum+=j
print(sum)


t=(1,2,3,4,5,6,7,8,9,10,11)
for n in t:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n,end=" ")

# find common 
l=[1,2,3,4,5]
s={3,4,5,6}
t=(2,3,5,7)
t1=(set(l))
t2=(set(t))
print(tuple(t1&s&t2))

#count of unique elements
t=(1,2,2,3,4,4,5)
count=0
for i in t:
    if count==1:
        break
print(i,end="")

#ele not in list
l=[1,2,3,4,5]
s={3,5}
s1=set(t)
t=tuple(s1-s)
print(t)
