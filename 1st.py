print("name: M. Keerthi")
print("college name: ST. Martins engineering college") 
print("branch: CSE(AI&ML)")
'''name=input("enter name:")
age=int(input("enter age:"))
print(name)
print(age)

x=int(input("enter 1st number: "))
y=int(input("enter 2nd element: "))
print("add:",x+y)
print("sub:",x-y)
print("mul:",x*y)
print("div:",x/y)
print("floordiv:",x//y)
print("modulo:",x%y)
'''


'''a=10
b=6
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
'''

a=10
b=15
print(a>b and b!=a)
print(a<b and b>=a)
print(a<=b and b==a)
print(a>b & b<a)

c=3
b=5
print(c==b or c+b==8)
print(c<b or c>b)
print(c+b==8 or b-c==2)
print(not c)

# assignment operators
x=7
x+=10
print(x)
x-=4
print(x)
x*=2
print(x)
x/=7
print(x)
x%=7
print(x)
x//=4
print(x)

# area of rectangle perimeter of rectangle
l=10
b=15
print("area of rectangle:",l*b)
print("perimeter of rectangle:",2*(l+b))

r=3
print("area of circle:",3.14*r*r)
print("perimeter:",2*3.14*r*r)

b=3
a=4
c=5
print("area of triangle:",1/2*b*a)
print("perimeter:",a+b+c)

'''calculate simple intrest
convert celius to farenheit
convert fahrenheit to celius
avg of 3 numbers, 5 numbers
swap two numbers
'''
p=1000
t=34
r=25
print("simple intrest:",p*t*r/100)

#celcius to fahrenheit
c=68
print(c*9/5+32)
# f to c
f=32
print(f-32*5/9)

a=2
b=3
c=4
print((a+b+c)/3)

a=1
b=2
c=3
d=4
e=5
print((a+b+c+d+e)/5)

a,b= 10,5
a,b==b,a
print("after swap:", (b,a))



x = 10
y = 2
x, y = y, x
print("after swapping of 2 numbers:", x, y)