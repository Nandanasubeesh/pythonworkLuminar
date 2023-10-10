from json import load
path="C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\modules\\read_fromjson\\movies\\countries\\countries.json"

with open(path,encoding="utf-8") as f:
    countries=load(f)
#print country names
#country_name=[c.get("name") for c in countries]
#print(country_name)
#how many countries
#print(len(countries))

pop_name=[c.get("name") for c in countries if c.get("population")<4000000]
print(pop_name)
#indepent value
#independent_value=[c.get("name") for c in countries if c.get("independent")==False]
#print(independent_value)

#demonym=[c.get("demonym")for c in countries]
#print(demonym)

#population_max=max(countries,key=lambda c:c.get("population"))

#print(population_max.get("name"))

#start_withc=[c.get("name") for c in countries if c.get("name").startswith("C")]
#print(start_withc)

#name_capital=[[c.get("name"),c.get("capital")]for c in countries]
#print(name_capital)

#c_with_borders=[ c for c in countries if "borders" in c]
#max_border_country=max(c_with_borders,key=lambda c:len(c.get("borders")))
#print(max_border_country.get("name"))
#sharing borders with india
#india_borders=[c.get("borders")for c in countries if c.get("name")=="India"][0]
#india_border_names=[ c.get("name")for c in countries if c.get("alpha3Code") in india_borders]
#print(india_border_names)
#print regions
#region_name={c.get("region")for c in countries}
#print(region_name)

#nativenames





asia 