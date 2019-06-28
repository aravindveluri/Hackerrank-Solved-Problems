def beautifulTriplets(d, arr):
    triples = 0
    for idx, val in enumerate(arr):
        temp = val
        count1 = arr.count(temp)
        print "temp, v1: ", (temp, count1)
        if temp+d in arr[idx+1:]:
            temp += d
            idx2 = arr.index(temp)
            count2 = arr.count(temp)
            print "temp, v2: ", (temp, count2)
            if temp+d in arr[idx2+1:]:
                temp += d
                count3 = arr.count(temp)
                print "temp, v3: ", (temp, count3)
                triples += 1#count1 * count2 * count3
            else:
                continue
        else:
            continue
    return triples
print beautifulTriplets(3, [1, 6, 7, 7, 8, 10, 12, 13 ,14, 19])