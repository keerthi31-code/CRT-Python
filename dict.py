# dictionaries - stores data as key: value
'''
{key:value}

d={}
{"name": "rani}
  key     : value



'''
student={
    "name": "rani",
    "age":22,
    "age":23
}
print(student)
print(student["name"])
print(student.get("name"))
# add key and value pair to dict
student["city"]='hyderabad'
print(student)
#delete - key:value pair
del student["name"]
print(student)
student .pop("age")
print(student)

# only key values printing
student={
    "name": "keerthi",
    "age":21
}
print(student.keys())
print(student.values())

#TRAVESRSING IN A DICTIONARY -- only travers in key part

student={
    "name": "keerthi",
    "age":21
}
for k in student:
    print(k)

student={
    "name": "keerthi",
    "age":21
}
for i in student.values():
    print(i)

# traverse through key part and value part
student={
    "name": "keerthi",
    "age":21
}
for i,j in student.items():
    print(i,j)
# in values we can give list values also.

#USER INPUT:
#n=int(input())
# m={
#     #empty dict {keerthi:21,mansa:20}
# }
# for i in range(n):
#     name=input() #keerthi
#     age=input() #21
#     m[name]=age #m[keerthi]=21
# print(m)

# n=int(input())
# dict={
# }
# for i in range(1,n):
#     num=input()
#     dict[num]=i*i
# print(dict)

s='banana'
dict={   
}
for ch in s:
    if ch in dict:
        dict[ch]+=1 
    else:
        dict[ch]=1 
print(dict)

s='banana'
d={
    #{b:1,a:3,n:2}
}
for ch in s:
    d[ch]=d.get(ch,0)+1 # d[b]=0+1=1
                        # d[a]=0+1=1 ---- d.get(n,0)=1- 1+1=2
                        # d[n]=0+1=1
print(dict)
    
'''
1)d={'a':10,'b':20,'c':30}
o/p 60 --sum of values
2)o/p 30 -- max value
3)o/p 3 -- count keys

4)most frequent char 
s='banana'
o/p a

5)nums=[1,2,3,4,5,6]
{"even":3
"odd" :3
}

6) find duplicates ele l=[1,2,3,2,4,1,5]
o/p 1,2
'''
n={
    'a':10,
    'b':20,
    'c':30
}
s=0
for i in n.values():
    s+=i
print(s)

d={
    'a':10,
    'b':20,
    'c':30
}
l=0
for i in d.values():
    if l>i:
        i=l
print(i)

l=0
mc=''
for i in d:
    if d[i]>l:
        i=d[i]
        mc=i
print(mc)

n={
    'a':10,
    'b':20,
    'c':30
}
count=0
for i in d.keys():
    count+=1
print(count)


s='banana'
dict={   
}
for ch in s:
    if ch in dict:
        dict[ch]+=1 
print(ch)

s='banana'
d={
}
for ch in d.values():
    d[ch]+=1
print(ch)


# nums=[1,2,3,4,5,6]
# d={
#     'even':0,
#     'odd':0
# }
# count=0
# for i in nums:
#     if i%2==0:
#         d["even"]+=1
#     else:
#         d["odd"]+=1
# print(d)    


# l=[1,2,3,2,4,1,5]
# for i in l:
#     d[i]=d.get(i,0)+1
# print(d)
# for k in d:
#     if d[k]>1:
#         print(k,end=" ")

num=[1,2,7,11,15]
target=9
d={

}
for i in range(len(num)): # i value index , num[i]=numbers
    x=target-num[i]
    if x in d:
        print(d[x],i)
    else:
        d[num[i]]=i
    
l=["eat","tea","tan","ate","nat","bat"]
d={
}
for i in l:
    key=tuple(sorted(i))
    if key not in d:
        d[key]=[]
    d[key].append(i)
print(list(d.values()))

logs=[{"km":200,
       "litre":5},
       {"km":350,"litre":8}]
tk=0
tl=0
for i in logs:
    tk+=i["km"]
    tl+=i["litre"]
print(tk/tl)

arr=[(3,1),(2,5),(3,0),(2,1)]
arr.sort(key=lambda t:(t[0],-t[1])) #both dec means both minus , in which ele we want decending order their we have to put minus
print(arr)






