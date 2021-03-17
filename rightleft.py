a=[2,3,4,5,7]
len1=3
tem=[]
i=0
while i <len(a):
    if a[i]==len1:
        break
    else:
        tem.append(a[i])
    i+=1
print(tem)