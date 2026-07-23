'''
#dec to binary
n=10
x=" "
while n>0:
    x=str(n%2)+x # 10%2+10
    n=n//2 #10//2=5 
print(x)


#binary to dec

s=1010
d=0
pow=0
for i in range(len(s) -1,-1,-1):
    d+=int(s[i])*(2**pow)
    pow+=1
print(d)

# dec to octal
n=23
x=" "
while n!=0:
    x=str(n%8)+x
    n=n//8
print(x)


# octal to decimal

s=325
d=0
pow=0
for i in range(len(s) -1,-1,-1):
    d+=int(s[i])*(8**pow)
    pow+=1
print(d)

# dec to hexadecimal
n=242
x=" "
hexa='0123456789ABCDEF'
while n>0:
    x=hexa[n%16]+x
    n=n//16 
print(x)


#hexa to decimal

s=input()
h=0
hexa='0123456789ABCDEF'
for ch in s.upper():
    h = h * 16 + hexa.index(ch)
print(h)
# mam 
h=input().upper()
digits="0123456789ABCDEF"
decimal=0
pow=0
for i in range(len(h) -1,-1,-1):
    decimal+=digits.index(h[i]) * (16**pow)
    pow+=1
print(decimal)


#Binary to octal
n=(input())
d=0
pow=0
for i in range(len(n) -1,-1,-1):
    d+=int(n[i]) * (2**pow)
    pow+=1
    
octal=""
if d==0:
    octal='0'
else:
    while d!=0:
        rem=d  % 8
        octal=str(rem)+octal
        d=d//8
print(octal)

#octal to binary

n=input()
d=0
pow=0
for i in range(len(n) -1,-1,-1):
    d+=int(n[i])*(8**pow)
    pow+=1
x=""
if d==0:
    x='0'
else:
    while d!=0:
        rem=d%2
        x=str(rem)+x
        d=d//2 
print(x)


# binary to hexa
n=input()
d=0
pow=0
for i in range(len(n) -1,-1,-1):
    d+=int(n[i]) * (2**pow)
    pow+=1
x=""
hexa='0123456789ABCDEF'
if d==0:
    x='0'
else:
    while d!=0:
        rem=d%16
        x=hexa[rem]+x
        d=d//16
print(x)

# hexa to binary
h=input().upper()
digits="0123456789ABCDEF"
decimal=0
pow=0
for i in range(len(h) -1,-1,-1):
    decimal+=digits.index(h[i]) * (16**pow)
    pow+=1
x=""
if decimal==0:
    x='0'
else:
    while decimal!=0:
        rem=decimal%2
        x=str(rem)+x
        decimal=decimal//2 
print(x)

#OCTAL -- HEXA DECIMAL
n=input()
d=0
pow=0
for i in range(len(n) -1,-1,-1):
    d+=int(n[i])*(8**pow)
    pow+=1

x=" "
hexa='0123456789ABCDEF'

if d==0:
    x='0'
else:
    while d!=0:
        rem=d%16
        x=hexa[rem]+x
        d=d//16 
print(x)


h=input().upper()
digits="0123456789ABCDEF"
decimal=0
pow=0
for i in range(len(h) -1,-1,-1):
    decimal+=digits.index(h[i]) * (16**pow)
    pow+=1

x=" "
if decimal==0:
    x='0'
else:
    while decimal!=0:
        rem=decimal%8
        x=str(rem)+x
        decimal=decimal//8
print(x)

n=int(input())
count=0
while n>0:
    count+=1
    n=n>>1
print(count)
'''

n=int(input())
count=0
while n>0:
    if n&1==1:
        count+=1  
    n=n>>1  
print(count)

n=int(input())
count=0
while n>0:
    if n&1==0:
        count+=1
    n=n>>1
print(count)