#SW
def max_sum(arr,k):
    max_sum=0
    window_sum=0
    for i in range(k):
        window_sum+=arr[i]
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i]
        window_sum-=arr[i]
        max_sum=max(max_sum,window_sum)
    return max_sum
arr=[2,1,5,1,3,2]
k=3
print(max_sum(arr,k))



#complete slicing
def sum_m(arr,k):
    max_sum=0
    for i in range(len(arr)-k):
        current_sum=sum(arr[i:i+k])
        max_sum=max(max_sum,current_sum)
    return max_sum
arr=[2,1,5,1,3,2]
k=3
print(max_sum(arr,k))

#slicing and SW
nums=[2,1,5,1,3,2]
k=3
window_sum=sum(nums[:k])
max_sum=window_sum
for i in range(k,len(nums)):
    window_sum+=nums[i]
    window_sum-=nums[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)

s='abababd'
p='ab'
k=len(p)
count=0
for ch in range(len(s)-k+1):
    if s[ch:ch+k]==p:
        count+=1
print(count)



