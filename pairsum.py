def checksum(list1,sum1):
    list1.sort()
    maxnumber=len(list1)-1
    minnumber=0
    while minnumber<maxnumber:
        if list1[minnumber]+list1[maxnumber]==sum1:
            print("pair found",list1[maxnumber],list1[minnumber])
        if list1[minnumber]+list1[maxnumber]<sum1:
            minnumber+=1
        else:
            maxnumber-=1

list1=[]
num=int(input("how many element you want in list"))
for i in range(num):
    num1=int(input("enter the number"))
    list1.append(num1)
sum1=int(input("enter the number for sum"))
checksum(list1,sum1)