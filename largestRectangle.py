x = []
def largestRectangle(h):
    if len(h) == 1:
        x.append(h[0])
        return 1
    x.append(min(h) * len(h))
    idx = h.index(min(h))
    h.remove(min(h))
    if idx == 0 or idx == len(h):
        largestRectangle(h)

    else:
        largestRectangle(h[:idx])
        largestRectangle(h[idx:])
    #return 0
    
largestRectangle([1,7,3,4,4,5])
print max(x)