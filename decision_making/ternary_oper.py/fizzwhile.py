start=1
end=50
while(start<=end):
    if(start%15==0):
        print("fizzbuzz")
    elif(start%5==0):
        print("buzz")
    elif(start%3==0):
        print("fizz")
    else:
        print(start)
    start+=1