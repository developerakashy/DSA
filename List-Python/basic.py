#element addition in list
l = [10,20,30,40,50]

print("l:",l)

l.append(30)
print(l)

l.insert(1,15)
print(l)

print(l.count(30))
print(l.index(30)) #only works for if element is present or error will be thrown
print(l.index(30,4,7))

#removal of list

l1 = [10,20,30,40,50,60,70,80]
print("l1:",l1)

l1.remove(20)#only works for if element is present
print(l1)

print(l1.pop())
print(l1)

print(l1.pop(2))
print(l1)

del l1[2]
print(l1)

del l1[0:2]
print(l1)


#some general purpose functions
l2 = [20,10,30,80,59,60]
print("l2:",l2)

print("Minimum:",min(l2))

print("Maximum:",max(l2))

print("Sum:",sum(l2))

l2.reverse()
print("Reverse:",l2)

l2.sort()
print("Sorted:",l2)
