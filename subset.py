

def Subset(arr1,arr2,arr1_size,arr2_size) : 
    count=0
    dir={} 
    for i in range(arr1_size): 
        if arr1[i] not in dir: 
            dir[arr1[i]] = 0
        dir[arr1[i]] += 1
    for i in range(arr2_size):  
        if arr2[i] not in dir: 
            count += 1
            break  
        else : 
            dir[arr2[i]] -= 1
              
            if (dir[arr2[i]] == 0): 
                dir.pop(arr2[i]) 
    return count  
      

size_of_array1 = int(input("enter the array size 1"))
arr1=[int(input()) for each in range(size_of_array1)]
size_of_array2 = int(input("enter the array size "))
arr2=[int(input()) for each in range(size_of_array2)]
  
status = Subset(arr1, arr2, size_of_array1, size_of_array2)
if status==0:
    print("arr2[] is subset of arr1[] ") 
else: 
    print("arr2[] is not a subset of arr1[]") 
