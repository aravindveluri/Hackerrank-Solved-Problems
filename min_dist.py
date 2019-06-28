def minimumDistances(a):
    l = []
    for idx, val in enumerate(a):
        #print 'idx', idx,'val', val
        try:
            #print 'index val', a[idx+1:].index(val) + 1
            l.append(a[idx+1:].index(val) + 1)
        except ValueError:
            pass
    if len(l) != 0:
        return min(l)
    return -1

print minimumDistances([3, 2, 1, 2, 3])