s={1,2,2,1,3,4}
s=list(s)
print(s)

t1='python is a great programming language'
t2='many developers love python language'
#print(set(t1)&set(t2))
print(set(t1.split())&set(t2.split()))
