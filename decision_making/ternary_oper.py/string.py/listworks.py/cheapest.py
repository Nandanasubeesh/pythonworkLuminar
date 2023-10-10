expenses=[1000,2000,3000,500,4000]
min_exp=expenses[0]
for e in expenses:
    if e < min_exp:
        min_exp=e

print(min_exp)