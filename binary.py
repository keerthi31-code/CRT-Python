arr=[10,20,30,40,50,60,70,80]
target=80
l=0
r=len(arr)-1
while l<=r:
    mid=l+r // 2
    if arr[mid]==target:
        print("found")
        break
    elif arr[mid]>target:
        r=mid-1
    else:
        l=mid+1

