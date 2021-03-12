import sys

def secondmax(list,listsize):
    if listsize < 2:
        print("size of list shoulb be atleast two")
        return
    if listsize == 2:
        if list[0]==list[1]:
            print("both the no are same")
            return    
    Max = list[0]
    sec_max = list[0]
    for i in range(0,listsize):
        if list[i] > Max:
            sec_max=Max
            Max=list[i]
        elif list[i]<Max and list[i]>sec_max:
            sec_max =list[i]
    return print("the secondmax no is  ",sec_max)

def secondmin(list,listsize):
    if listsize < 2:
        print("size of list shoulb be atleast two")
        return
    if listsize == 2:
        if list[0]==list[1]:
            print("both the no are same")
            return    
    Min = sys.maxsize
    sec_min = sys.maxsize
    for i in range(0,listsize):
        if list[i] < Min:
            sec_min=Min
            Min=list[i]
        elif list[i]> Min and list[i]<sec_min:
            sec_min = list[i]
    if (sec_min == sys.maxsize):
        return print("no seconmin no ")
    else:
        return print("the secondmin no is  ",sec_min)


size_of_list = int(input("enter the list size "))
list1=[int(input()) for each in range(size_of_list)]
secondmax(list1,size_of_list)
secondmin(list1,size_of_list)
