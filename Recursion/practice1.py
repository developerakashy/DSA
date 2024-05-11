def num(n):
    if n == 0:
        return
    
    print(n)
    num(n-1)
    print(n)

print(num(10))