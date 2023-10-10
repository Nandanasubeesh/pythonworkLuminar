all_users=["mohanlal","fahad","unny","mamootty","nivin"]
nivin_friends=["mohanlal","unny","fahad"]
suggestion_list=[]
for n in  all_users:
    if n not in nivin_friends:
        suggestion_list.append(n)
      
suggestion_list.pop(suggestion_list.index("nivin"))   
print(suggestion_list)

       