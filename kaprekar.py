def digits(x):
    if x//10 == 0:
        return 1
    return 1 + digits(x//10)
def kaprekarNumbers(p, q):
    l = []
    for i in xrange(p, q+1):
        d = digits(i)
        x = i*i
        y=str(x)
        #print (y, y[len(y)-d:], y[:len(y)-d])
        #exc = y[:len(y)-d]
        if(i<4):
            if int(y[len(y)-d:]) == i:
                l.append(i)
        else:
            if int(y[len(y)-d:]) + int(y[:len(y)-d]) == i:
                l.append(i)
    return l
print kaprekarNumbers(1, 100)