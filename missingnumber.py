def getmissingnumber(list1):
    n = len(list1)
    totalofallnumber = (n+1)*(n + 2)/2
    sum_oflist1 = sum(list1)
    return  totalofallnumber-sum_oflist1

number=int(input("how many element you want in list"))
list1=[]
i=1
while i <=number:
    num=(int(input("enter the number")))
    list1.append(num)
    i+=1
print(list1)
missingNo = getmissingnumber(list1)
print(missingNo)
