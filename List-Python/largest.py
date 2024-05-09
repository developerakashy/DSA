def largest(l):
    if not l:
        return None
    larg = l[0]
    for i in range(1,len(l)):
        if larg < l[i]:
            larg = l[i]

    return larg

l = [12,45,34,87,24,90]
l = [78,78,5]
print(l)
print("Largest:",largest(l))


def second_largest(l):
    if not l:
        return None
    
    second_larg = None
    larg = l[0]

    for i in l[1:]:
        if larg < i:
            second_larg = larg
            larg = i
        elif i != larg:
            if second_larg == None or second_larg < i:
                second_larg = i
                
    return second_larg


print("second Largest:",second_largest(l))