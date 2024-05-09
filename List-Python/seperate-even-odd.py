def even_odd(l):
    even = []
    odd = []
    for num in l:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return  even, odd 

even, odd = even_odd([10,20,33,40])
print("Even: ",even)
print("odd: ",odd)


