l = [10,20,30,40,50]

print(l[0:5:1])
print(l[:5])
print(l[1:])
print(l[::-1])
print(l[-1:-6:-1])


l1 = [10,20,30]
l2 = l1[:]

t1 = (10,20,30)
t2 = t1[:]

s1 = "akash"
s2 = s1[:]

print(l2 is l1)
print(t2 is t1)
print(s2 is s1)