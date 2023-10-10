from json import load
path="C:\\Users\\win\\Desktop\\pythonwork\\decision_making\\ternary_oper.py\\string.py\\listworks.py\\dict_works.py\\assignment.py\\listofdict.py\\fileinputoutput\\modules\\read_fromjson\\movies\\mdb.json"

with open(path,encoding="utf-8") as f:
    movies=load(f)

#movie_name=[m.get("title") for m in movies]
#print(movie_name)

#year_filter=[m.get("title") for m in movies if m.get("year")=="2005"]
#print(year_filter)

#fun_movies=[m.get("title") for m in movies if "comedy" in m.get("genres")]
#print(fun_movies)

#lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
#print(lengthy_movie)
 
#genres={g for m in movies for g in m.get("genres") }
#print(genres)
#print comedy movies
#c_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres") and m.get("year")=="2015"]
#print(c_movies)

wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(wc)
