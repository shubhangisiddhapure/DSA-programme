list1=[]
num=int(input("how many element you want in list"))
for i in range(num):
    num1=int(input("enter the number"))
    list1.append(num1)
list1.sort()
if len(list1)<=1:
    print("noting to sort")
elif len(list1)<=2:
    print("second smallest number",list1[1],"second largest number",list1[0])
else:
    maxnumber=list1[-1]
    maxnum=maxnumber
    print(list1)
    i=0
    while i <len(list1):
        if list1[i]<maxnumber:
            sec_min=maxnumber
            maxnumber=list1[i]
        elif list1[i]<sec_min and list1[i]!=maxnumber:
            sec_min=list1[i]
        if list1[i]<maxnum:
            sec_maxnumber=list1[i]
        i+=1
    print("the second max number",sec_maxnumber,"the second min number",sec_min)
        
