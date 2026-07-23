# for i  in range(4):
#     print("*")

# for i in range(5):
#     print("*",end=" ")
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# n=4
# for i in range(1,n+1):
#     for j in range(i): 
#         print("*",end=" ")
#     print() 

# n=4
# for i in range(1,n+1):
#     for j in range(i):
        
#         print("*",end=" ")
#     print()



# n=4
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
# #         print(i,end=" ")
# #     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         i=j+1
#         print(i,end=" ")
#     print()


# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
        

# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         i=j+1
#         print(i,end=" ")
#     print()

# n=int(input())
# m=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(m,end=" ")
#         m+=1
#     print()


# ch=65
# print(chr(ch))

# n=int(input())
# for i in range(1,n+1):
#     ch=65
#     for j in range(i):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()


# n=int(input())
# for i in range(n):
#     if i == 0 or i==n-1:
#         print("*" *n)
#     else:
#         print("*" + " " * (n-2)+"*")

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n=int(input())
for i in range(1,n+1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))
print()

n=int(input())
for i in range(n,0,-1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))
print()



n=int(input())
for i in range(1,n+1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))
for i in range(n,0,-1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))
print()


n=int(input())
for i in range(n,0,-1):
        print(" "*(n-i),end=" ")
        print("*" *(2*i-1))
for i in range(1,n+1):
        print(" " * (n-i),end=" ")
        print("*" *(2*i-1))