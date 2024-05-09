def smaller_than(l,num):
    element = []
    for x in l:
        if x < num:
            element.append(x)
    
    return element

smaller_elements = smaller_than([10,8,9,4,20,32],10)
print(smaller_elements)