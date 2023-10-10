#given number is even or odd
a=int(input("Enter a number"))
def even_odd(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
even_odd(a)