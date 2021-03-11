def sort1(list1):
    lownumber=0
    highestnumber=len(list1)-1
    number=0
    while number<=highestnumber:
        if list1[number]==0:
            list1[lownumber],list1[number]=list1[number],list1[lownumber]
            lownumber+=1
            number+=1
        elif list1[number]==1:
            number+=1
        else:
            list1[number],list1[highestnumber]=list1[highestnumber],list1[number]
            highestnumber-=1
    print(list1)
list1=[]
num=int(input("how many element you want in list"))
for i in range(num):
    num1=int(input("enter the number"))
    list1.append(num1)
sort1(list1) 