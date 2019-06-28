def superdigit(n, k):
    sdigit = str(n)
    x = str(reduce(lambda a,b: int(a)+int(b), sdigit))
    while(int(x) > 10):
        x = str(reduce(lambda a,b: int(a)+int(b), x))
    x = x*k
    while (int(x) > 10):
        x = str(reduce(lambda a,b: int(a)+int(b), x))
    return x


#print superdigit('123', 2)