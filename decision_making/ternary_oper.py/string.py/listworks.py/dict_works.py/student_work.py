text="ABCDA"
wc={}
for ch in text:
    if ch in wc:
        print("first recursive function",ch)
        break
    else:
        wc[ch]=1
print(wc)
