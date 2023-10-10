def product(*args):
    res=1
    for n in args:
        res*=n
    return res
print(product(1,2,3,4,5,6))
