n = int(input("Enter a number: "))

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True

print("Normal: ",isPrime(n))



# x*x <= n divisors are always in pair

def efficient_isPrime(n):

    if n == 1:
        return False
    
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        
        i += 1

    return True

print("Efficient: ",efficient_isPrime(n))



def most_efficient_isPrime(n):

    if n == 1 :
        return False
    
    elif n == 2 or n == 3:
        return True
    
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
        i += 6

    return True

print("Most efficient: ",most_efficient_isPrime(n))