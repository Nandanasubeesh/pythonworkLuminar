from re import *
text="abababcdab"
matcher=finditer("ab",text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)

for re import *
text="abcdABCD7e9fk"
pattern="[a-z]"
#pettern="[o-9]" chk for digits
# pattern="[a-z]" chk for lower case alphabets
#pattern=["[A-Z]"] chk for upper case alphbaets
#pattern"[a-zA-Z] chk for both upper and lower case/all alphabets
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


#pattern="[a-zA-Z0-9]" print all alphanumeric characters
#pattern="[^0-9]" excluding digits
#pattern="[^A-za-z0-9]"
pattern="[aeiouAEIOU]"
[D] exclude d
consanants
