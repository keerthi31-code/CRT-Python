'''n=int(input("enter the num: "))
for i in range(1,n):
    print(i)


n=int(input())
for i in range(1,n):
    if (i%2==0):
        print(i)
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    

i=1
while i<=10:
    print(i)
    i+=1


n=int(input()
sum=0
for i in range(1, n+1):
    sum+=i
print(sum)

# n=int(input())
# num=0
# while num==num%10:
#     rev=num//10
#     rev=rev+num*
#     print(rev)
rev=0
n=123
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

sum=0
n=123
while n!=0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)


n=121
temp=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==temp:
    print(True)
else:
    print(False)  

n=1234
pro=1
while n!=0:
    rem=n%10
    pro=pro*rem
    n=n//10
print(pro)

count=0
n=123
while n!=0:
    rem = n%10
    count+=1
    n=n//10
print(count)


num=int(input())
for i in range(1,num+1):
    if i*i==num:
        print("yes")
        break
else:
    print("no")  

n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("yes")
else:
    print("no")
'''
'''
n=int(input())
for i in range(1,n):
    if n & 1 ==0:
        print("yes")
        break
if n & 1!=0:
        print("no")


n=int(input())
for i in range(n+1):
    if n == 2**i:
        print("yes")
        break
else:
    print("no")
'''


n=int(input())
while n>1:
    if n%2!=0:
        break
    n=n//2
if n==1:
    print("yes")
else:
    print("no")


n=int(input())
temp=n
count=0
while temp>0:
    count+=1
    temp=temp//10
temp1=n
sum=0
while temp1>0:
    digit=temp1%10
    sum=sum+digit**count
    temp1=temp1//10
if sum == n:
    print("yes")
else:
    print("no")