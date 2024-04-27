def isPrime(n):
    for i in range(2,n):
        
        if n % i == 0:
            return False
        
    return True


n = int(input("Enter a number: "))
array = []
def prime_factorization(n):

    for i in range(2,n+1):
        x = i
        if isPrime(i):
            while n % x == 0:
                x = x * i
                array.append(i)

prime_factorization(n)
print("Prime factors:",array)

