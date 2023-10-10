text="aeiou dechjihuh"
v_count=0
c_count=0
#print vowel count and consanant count 
for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1

    elif ch !=" ":
        c_count+=1

print("vowel count",v_count)
print("consanant count",c_count)