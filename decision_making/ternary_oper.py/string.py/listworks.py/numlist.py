numbers=[1,4,10,11,12]

even_list=0
odd_list=0

for n in numbers:
    even_list.append(n) if n %2==0 else odd_list.append(n)
    print(n)