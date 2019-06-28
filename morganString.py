def morganAndString(a, b):
    s = ''
    while len(a)!=0 and len(b)!=0:
        if a == b:
            s += a[0]
            a = a[1:]
            b = b[1:]
        if strcheck(a, b) == 0:
            s += a[0]
            a = a[1:]
        if strcheck(a, b) == 1:
            s += b[0]
            b = b[1:]
    return s

def strcheck(a, b):
        if a[0]>b[0] and len(a)!=0 and len(b)!=0:
            a = a[1:]
            print "sumn"
            return 0
            
        if a[0]<b[0] and len(a)!=0 and len(b)!=0:
            b = b[1:]
            return 1#s += b[0]
        if len(a)==0 and len(b)==0:
            return -1    
        if a[0]==b[0]:
            strcheck(a[1:], b[1:])
                    
        return -1
        
print morganAndString('JACK', 'DANIEL')