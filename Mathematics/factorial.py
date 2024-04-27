n = int(input("Enter a number: "))

fact = 1
curr = 1

if n == 0:
    print("Factorial is: 1")
else:
    while curr <= n:
        fact *= curr
        curr += 1
    
    print("Factorial is: ",fact)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Reccursive way: ",factorial(n))