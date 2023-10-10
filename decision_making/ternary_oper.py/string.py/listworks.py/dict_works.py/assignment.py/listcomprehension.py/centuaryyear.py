years=[ y for y in range (1800,2026)]

#century_years=[ y for y in years if y%100==0]
#print(century_years)

non_century=[ y for y in years if y%100!=0]
print(non_century)