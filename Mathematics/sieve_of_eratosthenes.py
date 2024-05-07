n = int(input("Enter a number: "))

def isPrime(num):

    if num == 1:
        return False
    
    if num == 2 or num == 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5

    while (i * i <= num):
        if num % i == 0 or num % (i+2) == 0:
            return False
    
        i += 6

    return True

arr = []

def primeDivisor(n):

    for i in range(2, n + 1):
        if isPrime(i):
            arr.append(i)
        
primeDivisor(n)

print("PimeDivisor:",len(arr))




arr1 = []
def sieve(n):
    if n <= 1:
        return
    
    numArr = [True] * (n+1)

    i = 2

    while (i * i <= n):
        if numArr[i]:

            for j in range(i * i, n + 1, i):
                numArr[j] = False

        i += 1

    
    for i in range(2, n+1):
        if numArr[i]:
            
            arr1.append(i)

sieve(n)
print("sieve1:",len(arr1))




arr2 = []
def efficientSieve(n):
    if n <= 1:
        return
    
    numArr = [True] * (n+1) 

    i = 2

    while (i <= n):
        if numArr[i]:
            arr2.append(i)

            for j in range(i * 2, n + 1, i):
                numArr[j] = False

        i += 1

efficientSieve(n)
print("sieve2:",len(arr2))

