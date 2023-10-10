f=open("C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\numbers.txt","r")
numbers=[line.rstrip("\n") for line in f]
print(numbers)

#for n in numbers:
    #if n.startswith("kl"):
        #print(n)
kerala_reg=[n for n in numbers if n.startswith("kl")]
print(kerala_reg)