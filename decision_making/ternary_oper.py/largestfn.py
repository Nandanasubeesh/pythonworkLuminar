#largest among three numbers using fn
def largest(a,b,c):
    if(a>b) and (a>c) :
        print("a is largest")
    elif (b>c) and (b>a):
        print("b is largest")
    else:
        print("c is largest")

largest(10,20,30)
        