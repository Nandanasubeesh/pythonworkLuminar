txt="pycharm is an ide"
words=txt.split(" ")
total=0
for ch in words:
    total= len(ch) + total
print(total)


# txt="pycharm is an ide"
# vowels=["a","e","i","o","u"]
# v_count=0
# c_count=0
# for ch in txt:
#     if ch in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)



# txt="pycharm is an ide"
# vowels=["a","e","i","o","u"," "]
# c_count=0
# for ch in txt:
#     if ch not in vowels:
#         c_count+=1
# print(c_count)
