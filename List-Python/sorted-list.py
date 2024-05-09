def sort_check(l):
    i = 1

    while i < len(l):
        if l[i] < l[i-1]:
            return False

        i += 1
    
    return True

l = []

print(sort_check(l))



def is_sort(l):
    sl = sorted(l)

    if l == sl:
        return True
    else:
        return False
    
print(is_sort(l))