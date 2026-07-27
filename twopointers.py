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

def palindrome(arr):
    lft=0
    ryt=len(arr)-1
    while lft<ryt:
        lft+=1
        ryt-=1
        if arr[lft]!=arr[ryt]:
            return "not a palidrome"
            break        
    else:
        return "yes"
arr=[1,2,3,2,1]
print(palindrome(arr))

