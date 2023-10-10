f=open("C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\data.txt","r")
#lst=[]
#for line in f:
    #lst.append(line.rstrip("\n") )
    
#print(lst)
#longest_word=max(lst,key=lambda w:len(w))
#print(longest_word)

words=[line.rstrip("/n") for line in f]
longest_word=max(words,key=lambda w:len(w))
print(longest_word)