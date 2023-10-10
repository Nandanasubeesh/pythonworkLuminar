limit=100

prev=0
current=1


print(prev,current,"end")
for i in range(1,limit+1):
    sum=prev+current
    prev=current
    current=sum
    if sum<=limit:
        print(sum)
    else:
        break

   
