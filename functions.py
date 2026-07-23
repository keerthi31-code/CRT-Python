def hello_world():
    print("HELLO WORLD")
hello_world()

def add(a,b):
    return a+b
print(add(2,3))

x=20
def show():
    x=10
    print(x)
show()
print(x)


#check even or odd
def check(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
print(check(4))
print(check(3))

def square(n):
    
        return n**2
print(square(5))

def max_num(a,b):
    if a>b:
        return a
    else:
        return b
print(max_num(12,2))

def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(maximum(3,5,6))


'''
reverse of number
count number of digits
sum of digits
armstrong number
perfect number
perfect square
power of 2
celsus to Fahrenheit
Fahrenheit to celsus 
leetcode : 1281, 258, 231, 1342
check if a number is prime or not
factorial of a number
fibonacci series (0, 1, 1, 2, 3, 5, .....)
'''
#questions 
# reverse of number
def reverse_num(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem   
    return rev
print(reverse_num(123))
    
def count_num(n):
    count=0
    while n>0:  #123>0
        rem=n%10 #123%10 = 3
        n=n//10 # 123= 123//10 =12
        count+=1    
    return count
print(count_num(123))


def sum_digits(n):
    sum=0
    while n!=0:
        rem=n%10
        n=n//10
        sum+=rem
    return sum
print(sum_digits(12345))


def prime_num(n):
    for i in range(2,n):
        if n%i==0 :
            return False
        else:
            return True
print(prime_num(6))

def factorial_num(n):
    fact=1
    for i  in range(1,n+1):
        fact=fact*i
    return fact
print(factorial_num(5))



def arm_strong(n):
    temp=n
    temp1=n
    count=0
    while n>0:
        count+=1
        n=n//10

    total=0
    while temp1>0:
        rem=temp1%10
        total=total+rem**count
        temp1=temp1//10
    return total==temp


print(arm_strong(153))


def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    else:
        return False
    
print(perfect_num(6))
print(perfect_num(8))