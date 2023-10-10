num=1634
sum=0
orginal=num

while(num!=0):
    last_digit=num % 10
    cube=last_digit**4
    sum=sum+cube
    num=num // 10

if(orginal==sum):
    print("armstrong")
else:
    print("not armstrong")