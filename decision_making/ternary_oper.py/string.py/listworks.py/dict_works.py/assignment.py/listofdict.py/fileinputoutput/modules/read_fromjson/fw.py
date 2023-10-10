from json import load
path="C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\modules\\read_fromjson\\data.json"
with open(path) as f:
    records=load(f)

#print(records)

#for f in records:
    #print(f.get("name"))

fw_names=[f.get("name") for f in records]

print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)