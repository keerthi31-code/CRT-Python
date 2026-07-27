def pointer(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        print(arr[left],arr[right])
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5]
print(pointer(arr))

def reverese(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5]
print(reverese(arr))
