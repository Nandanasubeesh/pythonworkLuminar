f_read=open("C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\num.txt")
odd_write=open("C:\\Users\\win\\Desktop\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\num.txt","w")
even_write=open("C:\\Users\\win\\Desktop\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\num.txt","w")

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")

    else:
        odd_write.write(str(num)+"\n")