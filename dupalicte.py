def dupalicateNo(list1):
    c=0 
    numberMap = {}
    for i in list1:
        if not i in numberMap:
            numberMap[i] = True
             
        else:
            z=i
            c+=1
    if c>=1:
        return z
num=int(input("how many element you want in list1"))
list1=[]
i=1
while i<=num:
    num1=int(input("enter the number"))
    list1.append(num1)
    i+=1
print(list1)
number=dupalicateNo(list1)
print(number)