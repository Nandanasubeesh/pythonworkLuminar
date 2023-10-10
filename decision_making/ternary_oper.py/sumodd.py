#print total sum of all odd numbers and even numbers from given start to end range

start=10
end=20
odd_sum=0
even_sum=0

while(start<=end):
    if (start%2==0):
        even_sum=even_sum+start
    elif (start%2!=0):
        odd_sum=odd_sum+start
        start+=1
print("even_sum",even_sum)
print("odd_sum",odd_sum)