text="i have car 2 bikes and 3 cycles"

words=text.split(" ")
for w in words:
    if w.isdigit():
        print(w)