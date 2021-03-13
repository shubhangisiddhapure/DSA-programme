def maxDiff(arr, n):
    maxnumber=0
    i=0
    j=1
    while i<n:
        if len(arr)<=1:
            pass
        elif arr[i]<arr[j]:
            diff=arr[j]-arr[i]
            if diff>maxnumber:
                maxnumber=diff
        i+=1
        j+=1
        if j>=n:
            break
    return maxnumber
num=int(input("how many element you want in array"))
arr=[]
i=1
while i <=num:
    num1=int(input("enter the numeber"))
    arr.append(num1)
    i+=1
print(arr)
n = len(arr) 
print(maxDiff(arr, n))