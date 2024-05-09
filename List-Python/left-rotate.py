l = [10,20,30,40,50]
print(l[1:] + l[0:1])

l2 = [1,2,3,4,5]
l2.append(l2.pop(0))
print(l2)

def left_rotate(l):
    start = l[0]

    for i in range(1,len(l)):
        l[i-1] = l[i]

    l[len(l) - 1] = start

    return l

l1 = [5,6,7,8,9,10]
print("Function Created:",left_rotate(l1))