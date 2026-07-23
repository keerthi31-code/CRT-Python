'''lst=list(map(int,input().split()))
print(sum(lst))

#sum of ele
lst=list(map(int,input().split()))
sum=0
for i in lst:
    sum+=i
print(sum)

#largest ele in lst

lst=list(map(int,input().split()))
l=0
for i in lst:
    if i>l:
        l=i
print(l)

#smallest ele
lst=list(map(int,input().split()))
s=lst[0]
for i in lst:
    if s>i:
        s=i
print(s)


#count
lst=[1,3,2,5,9]
count=0
for i in lst:
    count+=1
print(count)


lst=[5,3,2,6,4,8,7]
count=0
count1=0
for i in lst:
    if i %2==0:
        count+=1
    elif i%2!=0:
        count1+=1
print("even count: ",count)
print("odd count: ",count1)

lst=[5,3,2,6,4,8,7]
count=0
count1=0
for i in lst:
    if i %2==0:
        count+=1
    else:
        count1+=1
print("even:",count,"odd:",count1)

#second largest element
lst=list(map(int,input().split()))
l=0
s=0
for i in lst:
    if i>l:
        s=l
        l=i 
    elif l>i>s:
        s=i 
print(s)
'''
# remove duplicates
lst=[4,2,5,2,7,4,5,8]
l=[]
for i in lst:
    if i not in l:
        l.append(i)
print(l)

    #0,1,2,3,4,5,6,7,8
lst=[1,4,3,2,5,6,9,11,14]
sum=0
for i in range(len(lst)):
    if i%2!=0 and lst[i]%2==0:
        sum+=lst[i]
print(sum)

#even ele , even index
#odd ele, even index
#odd ele , odd index

#unique num-- non repeating elements
lst=[1,1,2,2,3,4,4,5]
for i in lst:
    if lst.count(i)==1:
        print(i, end=" ")

#building sunrise
lst=[3,4,5,4,7,6,2,3,6,8]
high=0
count=0
for i in lst:
    if i >high:
        count+=1
        high=i
print(count)


#left rotate array
arr=[1,2,3,4,5]
k=2
print(arr[k:]+arr[:k])

arr=[1,2,3,4,5]
k=2
print(arr[-k:]+arr[:-k])

x=[1,2,3,4,5,6,7,8,9,10,11,12]
res=[]
for i in x:
    if i%2==0:
        res.insert(0,i)
    else:
        res.append(i)
print(res)
    
arr=[1,0,2,0,4,0]
pos=[]
for i in arr:
    if i!=0:
        pos.append(i)
while len(pos)<len(arr):
    pos.append(0)  
print(pos)

def move_zeroes(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[pos]=arr[pos],arr[i]
            pos+=1
    return arr
arr=[1,0,2,0,4,0]
print(move_zeroes(arr))
