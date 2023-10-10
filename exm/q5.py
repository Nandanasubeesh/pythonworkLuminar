f=open("C:\\Users\\win\\Desktop\\pythonwork\\exm\\tyrecodes.txt","w")

from re import*
valid_tyrecode=(input("enter the tyre code"))
rule="[\d]{3}[\d]{2}[A-Z]\d{2}[\d]{2,3}[A-Z]*"
matcher=fullmatch(rule,valid_tyrecode)
print("valid" if matcher!=None else "invalid")
 
