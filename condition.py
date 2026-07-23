n=2
if n %2==0:
    print("even")
else:
    print("odd")

n=int(input("enter your age: "))
if n >=18:
    print("your eligible")
elif n==17:
        print("not eligible")
else:
        print("your minor")

marks=(int(input("enter marks: ")))
if marks >=90:
      print("A")
elif marks >=80:
      print("B")
elif marks >=70:
      print("c")
elif marks >=60:
      print("D")
else:
      print("F")

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
if a>b:
    print(a)
else:
    print(b)
    

a=5
b=9
c=3
if a>b and a>c:
    print("a")
elif b>c and b>a:
    print("b")
else:
    print("c")


w=int(input("enter the weight:"))
if w%2==0 and w>2:
    print("yes")
else:
    print("no the watremelon cannot divide into even half")

n=int(input("enter thr steps: "))
if n%5==0:
    print(n//5)
else:
    print(n//5+1) 

yr=int(input("enter the year: "))
if yr%400==0:
    print("leap year") 
else:
    print("not a leap year")  