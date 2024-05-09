l = [10,20,30,40,50]
l.reverse()
print(l)

l2 = [10,20,30,40,50]
new_l = list(reversed(l2))
print(new_l)

l3 = l2[::-1]
print(l3)


def rev(l):
    start = 0
    end = len(l)-1

    # for i in range(len(l)//2):
    while start < end:
        l[start],l[end] = l[end],l[start] 
        start += 1
        end -= 1

    return l
l4 = [1,2,3,4]
print("Function Created:",rev(l4))