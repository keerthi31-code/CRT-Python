
s='python'
print(s[0])
print(s[3])
print(s[1])
print(s[-1])
print(s[-3])
print(s[-6])

print(s[1:4:1])
print(s[2:])
print(s[0:])
print(s[3:])
print(s[::2])
print(s[:4])
print(s[:-1])

print("yt" in s)
print('iyt'  not in s)
a='keerthi'
b='keerthiluu'
print(a is b)

s1='python'
s2='pythoni'
print("yt" in s)
print("yh" in s)
print("yt" not in s)
print("yh"not in s)
print(s is s1)
print(s is not s1)
print(s1 is s2)
print(s1 is not s2)

a='Hello HI'
b='world'
print(a+b)
print(a+" "+b)
print(a*3)
print("hi" *3)
print(len(a))
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.swapcase())

x="ilikepython"
x1='123'
print(x.replace("python","DSA"))
print(x.find("h"))
print(x.index("l"))
print(x.count("i"))
print(x.isalpha())
print(x1.isdigit())
print(x.isalnum())
print(x.islower())
print(x.isupper())
print(x.isspace())
print(" ".isspace())



s='keerthi'
print(s[::-1])

x='python'
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")

    
s1='python'
rev=" "
for ch in s1:
    rev= ch+rev
print(rev)

s2='keerthi'
count=0
for ch in s2:
    if ch in 'aeiouAEIOU':
        count+=1
print(count)

s3='keerthi'
count=0
for ch in s3:
    if ch not in  'aeiouAEIOU':
        count+=1
print(count)

str=input()
rev=str[ : :-1]
rev = rev
if str == rev:
    print("palindrome")
else:
    print("no")


x='keerthi'
count=0
for ch in x:
    count+=1
print(count)

x='NavYa'
count=0
count1=0
for ch in x:
    if ch in x.upper():
        count+=1
    else:
        count1+=1
print(count)
print(count1)


x='manasa'
count=0
for ch in x:
    if ch in x.lower():
        count+=1
print(count)



x="i like python"
print(x.replace(" ",""))




s='college'
x=' '
for ch in s:
    if ch not in x:
        x+=ch
print(x)
print(len(x))


s="college"
x=" "
for ch in s:
    if ch not in x:
        x+=ch
        print(ch,s.count(ch))



s1='college'
x=''
for ch in s1:
    if ch not in x:
        x+=ch
        break
print(ch,s1.count(ch))

x=input()
for ch in x:
    if x.count(ch)==1:
        print(ch)
        break
else:
    print("no")  
    

s='computer'
s1='moputceri'
if (sorted(s))==(sorted(s1)):
    print("yes")
else:
    print("no")