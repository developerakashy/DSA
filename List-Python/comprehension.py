def smaller_than(l,num):
    return [x for x in l if x < num ]

def even_odd(l):
    return [x for x in l if x % 2 == 0],[x for x in l if x % 2 != 0]

even,odd = even_odd([10,23,45,22,40])
print("Even:",even)
print("odd:",odd)

print("Smaller:",smaller_than([10,3,6,23,5],10))

l1 = ["Google","Gmail","Photos","Youtube","Message","Drive"]

l2 = [x.upper() for x in l1 if x.lower().startswith("g")]

print(l2)

#set comprehension
l3 = [10,27,30,40,55,60,27,80,90,100]

set1 = { x for x in l3 if x % 2 == 0 }
set2 = { x for x in l3 if x % 2 != 0 }

print("Even:",set1)
print("Odd:",set2)

# dictionary comprehension
l4 = [1,2,3,4,5,6]

dict1 = {x:x**3 for x in l4}

dict2 = {x:f"ID{x}" for x in range(6)}

l5 = ["Google", "Bing", "DuckDuckGo"]
dict3 = {l4[i]:l5[i] for i in range(len(l5))}

dict4 = dict(zip(l4,l5))

print(dict1)
print(dict2)
print(dict3)
print(dict4)

#inverting dictionary
d2 = {v:x for (x,v) in dict4.items()}

print(d2)