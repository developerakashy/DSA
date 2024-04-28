n = int(input("Enter a number: "))

def isPrime(num):

    if num == 1:
        return False
    
    if num == 2 or num == 3:
        return False
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5

    while (i * i <= num):
        if num % i == 0 or num % (i+2) == 0:
            return False
    
        i += 6

    return True

arr = []

def sieve(n):

    for i in range(2, n + 1):
        if isPrime(i):
            arr.append(i)
        
sieve(n)

print(arr)
