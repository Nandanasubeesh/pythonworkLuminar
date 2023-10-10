list=[2,1,5,3,5,7,7,6,3]
list.sort()
for i in range(0,len(list)-1):
    current=list[i]
    next=list[i+1]
    if current==next:
        print(current)



