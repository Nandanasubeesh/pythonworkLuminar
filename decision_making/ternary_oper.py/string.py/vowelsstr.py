text="sunil gavaskar had a no-hold barred remark on overseas commandators"
#print words starting with vowels

words=text.split(" ")
vowels=["a","e","i","o","u"]
for w in words:
   if w[0].casefold() in vowels:
        print(w)
        



