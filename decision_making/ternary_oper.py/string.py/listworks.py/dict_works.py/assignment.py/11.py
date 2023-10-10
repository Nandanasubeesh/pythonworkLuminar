num_people=int(input("How many people do you want to invite"))
name=input("Enter the name")
for i in range(num_people):
    if num_people<10:
        print("[Name] has been invited")
    else:
        print("Too many people")